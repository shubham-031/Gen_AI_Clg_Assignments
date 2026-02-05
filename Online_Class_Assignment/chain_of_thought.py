# Chain of Thought Prompting example

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Chain of Thought prompting means breaking down the problem into smaller steps and reasoning through each step before arriving at the final answer.
SYSTEM_PROMPT="""
You are an expert coding assistant in resolving user queries using chain of thought prompting.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done, The PLAN can be multiple steps.
Once you think enough PLAN has been done, you will then OUTPUT the final answer.

Rules:
    - Strictly follow the given JSON format.
    - Only run one step at a time.
    - The sequence of steps should be START (Where user gives an input) -> PLAN (Where you plan the solution) -> OUTPUT (Where you give the final answer).

Output Format:
   {"step":"START" or "PLAN" or "OUTPUT",
   "content":"string"
   }

Examples:
   START: Hey , Can you solve 2 +3 * 5 /10 
   PLAN:{"step":"PLAN", "content":"seems like user intrested in solving a mathematical problem."}
   PLAN:{"step":"PLAN", "content":"looking at the problem i can see that according to BODMAS rule multiplication and division needs to be done first."}
   PLAN:{"step":"PLAN", "content":"Yes , BODMAS is correct here."}
   PLAN:{"step":"PLAN", "content":"So first I will solve 3 * 5 = 15"}
   PLAN:{"step":"PLAN", "content":"Next I will solve 15 / 10 = 1.5"}
   PLAN:{"step":"PLAN", "content":"Finally I will solve 2 + 1.5 = 3.5"}
   OUTPUT:{"step":"OUTPUT", "content":"Great we solved it! The final answer is 3.5"}
    """

response=client.chat.completions.create(
    model="gemini-3-flash-preview",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey , Write a code to add n numbers in js"}
    ]
)

print(response.choices[0].message.content)