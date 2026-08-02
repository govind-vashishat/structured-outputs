import os

from dotenv import load_dotenv
from openai import OpenAI

from sample_text import sample_text
from schema import Invoice

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.parse(
    model="gpt-5-mini",
    input=[
        {
            "role": "system",
            "content": "Extract the invoice information from the provided text."
        },
        {
            "role": "user",
            "content": sample_text
        }
    ],
    text_format=Invoice,
)

invoice = response.output_parsed

print(invoice)
print(type(invoice))
print(invoice.model_dump())