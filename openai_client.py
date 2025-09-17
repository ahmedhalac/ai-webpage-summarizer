from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL_NAME


class OpenAIClient:
    def __init__(self, api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL_NAME):
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name

    def summarize_website(self, website):
        system_prompt = """You are an assistant that analyzes the contents of a website
        and provides a short summary, ignoring text that might be navigation related.
        Respond in markdown."""

        user_prompt = f"You are looking at a website titled {website.title}"
        user_prompt += """\nThe contents of this website is as follows;
        please provide a short summary of this website in markdown.
        If it includes news or announcements, then summarize these too.\n\n"""
        user_prompt += website.text

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        response = self.client.chat.completions.create(
            model=self.model_name, messages=messages
        )

        return response.choices[0].message.content
