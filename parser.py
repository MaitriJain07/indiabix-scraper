from bs4 import BeautifulSoup
from urllib.parse import urljoin
from formatter import clean_node


def parse_questions(html):
    soup = BeautifulSoup(html, "lxml")

    questions = []

    blocks = soup.find_all("div", class_="bix-div-container")

    for block in blocks:

        # ------------------------
        # Question Number
        # ------------------------
        qno = block.find("div", class_="bix-td-qno")

        if qno:
            qno = qno.get_text(strip=True)
        else:
            qno = ""

        # ------------------------
        # Question Text
        # ------------------------
        qtext = block.find("div", class_="bix-td-qtxt")

        if qtext:
            qtext = qtext.get_text(" ", strip=True)
        else:
            qtext = ""

        # ------------------------
        # Options
        # ------------------------
        options = []

        for opt in block.find_all("div", class_="bix-td-option-val"):
            options.append(clean_node(opt).strip())

        # ------------------------
        # Correct Answer
        # ------------------------
        answer = ""

        hidden = block.find("input", class_="jq-hdnakq")

        if hidden:
            answer = hidden.get("value", "")

        # ------------------------
        # Explanation
        # ------------------------
        explanation = ""

        exp = block.find("div", class_="bix-ans-description")

        if exp:
            explanation = clean_node(exp).strip()

            if "Video Explanation:" in explanation:
                explanation = explanation.split("Video Explanation:")[0].strip()

        # ------------------------
        # Video
        # ------------------------
        video = ""

        for link in block.find_all("a", href=True):
            if "youtu" in link["href"]:
                video = link["href"]
                break

        questions.append(
            {
                "question_no": qno,
                "question": qtext,
                "options": options,
                "answer": answer,
                "explanation": explanation,
                "video": video,
            }
        )

    return questions


def get_next_page(html, current_url):
    soup = BeautifulSoup(html, "lxml")

    for a in soup.find_all("a", class_="page-link"):
        text = a.get_text(" ", strip=True)

        if "Next" in text:
            href = a.get("href")

            if not href or href == "#":
                return None

            return urljoin(current_url, href)

    return None
