import json

with open("data/knowledge_base.json", "r") as f:
    KB = json.load(f)

def retrieve_answer(query: str) -> str:
    q = query.lower()

    if "price" in q or "plan" in q:
        return (
            "AutoStream Pricing:\n\n"
            "Basic Plan:\n"
            "- $29/month\n"
            "- 10 videos/month\n"
            "- 720p resolution\n\n"
            "Pro Plan:\n"
            "- $79/month\n"
            "- Unlimited videos\n"
            "- 4K resolution\n"
            "- AI captions\n"
        )

    if "refund" in q:
        return KB["policies"]["refund"]

    if "support" in q:
        return KB["policies"]["support"]

    return "I can help with pricing, plans, or features. What would you like to know?"
