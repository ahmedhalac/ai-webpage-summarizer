# AI Webpage Summarizer

An AI-powered Python tool that fetches the content of a webpage, analyzes it using OpenAI's GPT models, and provides a concise summary in Markdown. Ideal for quickly understanding the key content of websites and any news or announcements.

---

## Features

- Fetches and parses webpage content using `requests` and `BeautifulSoup`.
- Cleans irrelevant HTML elements (`script`, `style`, `img`, `input`) for a cleaner text output.
- Generates AI-powered summaries using OpenAI GPT models.
- Outputs summaries in **Markdown**, rendered beautifully in the terminal using [Rich](https://github.com/Textualize/rich).

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/ai-webpage-summarizer.git
cd ai-webpage-summarizer
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file with your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=your_open_ai_model_here
```

## Note
Note that this will only work on websites that can be scraped using this simplistic approach.

Websites that are rendered with Javascript, like React apps, won't show up. See the community-contributions folder for a Selenium implementation that gets around this. You'll need to read up on installing Selenium (ask ChatGPT!)

Also Websites protected with CloudFront (and similar) may give 403 errors.

But many websites will work just fine!
