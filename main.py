import requests
from bs4 import BeautifulSoup
from IPython.display import display
from openai import OpenAI

from config import OPENAI_API_KEY

openai = OpenAI(api_key=OPENAI_API_KEY)

message = "Hello, GPT! This is my first message to you! Hi!"
response = openai.chat.completions.create(model="gpt-4o-mini",
                                          messages=[{"role": "user", "content": message}])

print(response.choices[0].message.content)
