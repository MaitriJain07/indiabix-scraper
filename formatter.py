from bs4 import NavigableString, Tag


def clean_node(node):
    """
    Recursively converts IndiaBIX HTML into readable text.
    """

    if isinstance(node, NavigableString):
        return str(node)

    if not isinstance(node, Tag):
        return ""

    # -----------------------
    # Special handling for fraction tables
    # -----------------------
    if node.name == "table" and "ga-tbl-answer" in node.get("class", []):

        rows = node.find_all("tr")

        if len(rows) >= 2:

            top = rows[0].find_all("td")
            bottom = rows[1].find_all("td")

            numerator = " ".join(
                td.get_text(" ", strip=True)
                for td in top
                if "ga-td-divident" in td.get("class", [])
            )

            denominator = " ".join(
                td.get_text(" ", strip=True)
                for td in bottom
                if "ga-td-divisor" in td.get("class", [])
            )

            if numerator and denominator:
                return f"{numerator}/{denominator}"

        return node.get_text(" ", strip=True)

    # -----------------------
    # Paragraphs
    # -----------------------
    if node.name == "p":
        return clean_children(node) + "\n"

    # -----------------------
    # Line breaks
    # -----------------------
    if node.name == "br":
        return "\n"

    return clean_children(node)


def clean_children(node):
    text = ""

    for child in node.children:
        text += clean_node(child)

    return text
