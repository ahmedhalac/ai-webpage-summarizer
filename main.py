from rich.console import Console
from rich.markdown import Markdown
from openai_client import OpenAIClient
from website import Website


def display_summary(url):
    website = Website(url)
    client = OpenAIClient()
    summary = client.summarize_website(website)
    console = Console()
    console.print(Markdown(summary))


display_summary("https://edition.cnn.com/")
