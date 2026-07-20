from scraper import fetch
from parser import parse_questions, get_next_page
from writer import save_json, save_markdown, save_prompt
url = input("Topic URL: ").strip()

all_questions = []

page = 1

while url:

    print(f"Scraping page {page}")

    html = fetch(url)

    questions = parse_questions(html)

    print(f"Found {len(questions)} questions")

    all_questions.extend(questions)

    next_url = get_next_page(html, url)
    print("Next URL:", next_url)
    url = next_url
    page += 1

topic = input("Topic name: ").strip()

save_json(topic, all_questions)
save_markdown(topic, all_questions)
save_prompt(topic, all_questions)
print()
print("Done!")
print("Total Questions:", len(all_questions))
