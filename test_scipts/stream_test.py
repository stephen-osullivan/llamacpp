from openai import OpenAI

"""
simple script to demonstrate receiving a stream from the llm endpoint
"""

client = OpenAI(base_url="http://0.0.0.0:8000/v1", api_key="sk-xxx") # dummy key
stream = client.chat.completions.create(
    model="can-write-anything-here",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Write an essay about llamas."}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")