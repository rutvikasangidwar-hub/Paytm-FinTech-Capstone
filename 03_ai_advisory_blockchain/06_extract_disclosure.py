import re
from disclosure_snippets import DISCLOSURE_SNIPPETS

def extract_signals(snippet: str) -> dict:
    text = snippet.lower()

    risk_flags = []
    if re.search(r"litigation", text):
        risk_flags.append("litigation")
    if re.search(r"regulatory|regulator|data-localization", text):
        risk_flags.append("regulatory")
    if re.search(r"top three customers|customer concentration|account for approximately", text):
        risk_flags.append("customer concentration")

    hedging = bool(re.search(r"assuming|cautiously|visibility", text))

    if re.search(r"confident|approved", text):
        sentiment = "confident"
    elif hedging:
        sentiment = "cautious"
    else:
        sentiment = "neutral"

    return {
        "risk_flags": risk_flags,
        "hedging_detected": hedging,
        "sentiment": sentiment,
    }

if __name__ == "__main__":
    for snippet in DISCLOSURE_SNIPPETS:
        doc_id = snippet.split(":", 1)[0]
        print(doc_id, "->", extract_signals(snippet))
