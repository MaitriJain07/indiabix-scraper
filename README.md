# IndiaBix Aptitude Scraper

A Python web scraper that extracts aptitude questions from IndiaBix and converts them into study-friendly Markdown, JSON and AI prompt files.

## Features

- Scrapes questions, options, answers and explanations
- Handles pagination
- Cleans HTML formatting
- Generates topic-wise study material

## Usage

Create virtual environment:

python3 -m venv venv

Install dependencies:

pip install -r requirements.txt

Run:

python3 main.py

Enter topic URL and topic name.

## Output

output/
 └── Topic/
      ├── Topic.md
      ├── Topic.json
      └── Topic_PROMPT.txt
