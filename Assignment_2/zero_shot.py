# zero shot prompting example

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#Zero shot prompting means directly giving the instructions to the model without any examples.
SYSTEM_PROMPT="You should only answers the coding related queshions. Do not ans the questions which are not related to coding. If the question is not related to coding, you will say sorry i am not able to help with that.Your name is Alexa and you are a coding expert."

response=client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "write a python code to transalate the word hello to hindi"}
    ]
)

print(response.choices[0].message.content)