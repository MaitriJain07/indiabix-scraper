import json
from pathlib import Path


def create_topic_folder(topic):
    """
    Creates:
    output/topic_name/
    """

    folder = Path("output") / topic
    folder.mkdir(parents=True, exist_ok=True)

    return folder



def save_json(topic, questions):
    folder = create_topic_folder(topic)

    filename = folder / f"{topic}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            questions,
            f,
            indent=4,
            ensure_ascii=False
        )



def save_markdown(topic, questions):
    folder = create_topic_folder(topic)

    filename = folder / f"{topic}.md"

    with open(filename, "w", encoding="utf-8") as f:

        f.write(f"# {topic}\n\n")

        f.write(f"Total Questions: {len(questions)}\n\n")

        f.write("---\n\n")


        for q in questions:

            f.write(f"## Question {q['question_no']}\n\n")


            f.write("### Question\n\n")
            f.write(q["question"] + "\n\n")


            f.write("### Options\n\n")

            letters = ["A", "B", "C", "D", "E"]

            for i, option in enumerate(q["options"]):
                f.write(f"- **{letters[i]}.** {option}\n")

            f.write("\n")


            f.write("### Correct Answer\n\n")
            f.write(f"✅ **{q['answer']}**\n\n")


            f.write("### Explanation\n\n")

            if q["explanation"]:
                f.write(q["explanation"] + "\n\n")
            else:
                f.write("No explanation available.\n\n")


            if q["video"]:

                f.write("### Video Explanation\n\n")
                f.write(q["video"] + "\n\n")


            f.write("---\n\n")



def save_prompt(topic, questions):

    folder = create_topic_folder(topic)

    filename = folder / f"{topic}_PROMPT.txt"


    with open(filename, "w", encoding="utf-8") as f:

        f.write(f"""
You are my aptitude teacher.

Topic: {topic}

I have scraped {len(questions)} aptitude questions from IndiaBIX.

Teach me this topic before solving questions.

Explain:

1. Core theory concepts
2. Important formulas
3. Shortcuts and tricks
4. Common patterns asked in placements
5. How to identify which method to use
6. Common mistakes students make

Then analyze every question:

For each question:
- Explain the approach
- Explain why the answer is correct
- Mention shortcut methods if available
- Mention the concept tested

Prepare me for placement aptitude exams.
""")
