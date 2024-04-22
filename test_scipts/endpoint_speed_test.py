from openai import OpenAI
import concurrent.futures
import time

client = OpenAI(base_url="http://0.0.0.0:8000/v1", api_key="sk-xxx") # dummy key


def get_response(name):
    t0 = time.time()
    response = client.chat.completions.create(
        max_tokens=250,
        model="can-write-anything-here",
        messages=[ 
            {"role": "system", "content": "You are a story writing assistant."},
            {
                "role": "user",
                "content": "Write a story about llamas."
            }  
        ])
    return name, response, time.time() - t0


if __name__ == "__main__": 
    t0 = time.time()
    threads = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submit the tasks to the executor
        for i in range(10):
            threads.append(executor.submit(get_response, i))
            print('Submited thread', i)
            
        # print results as and when they come in
        for task in concurrent.futures.as_completed(threads):
            name, response, exec_time = task.result()
            message = response.choices[0].message.content
            print(f'Request {name}, time: {exec_time:.2f}, n_tokens = {response.usage.total_tokens}')
            #print(message)

    print('Total Execution time:', time.time()-t0)