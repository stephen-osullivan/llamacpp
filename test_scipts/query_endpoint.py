from openai import OpenAI

client = OpenAI(base_url="http://0.0.0.0:8000/v1", api_key="sk-xxx") # dummy key
response = client.chat.completions.create(
    model="can-write-anything-here",
    messages=[ 
        {"role": "system", "content": "You are a story writing assistant."},
        {
            "role": "user",
            "content": "Write a story about llamas."
        }  
    ],
)
print(response)

