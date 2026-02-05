import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

while(True):
    prompt = input("Enter your prompt (or type 'exit' to quit) 👉 ")
    if prompt.lower() == 'exit':
        break

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("🤖", response.choices[0].message.content)