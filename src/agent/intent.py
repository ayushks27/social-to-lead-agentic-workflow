import json
from langchain_google_genai import ChatGoogleGenerativeAI

# Gemini 1.5 Flash (as required by assignment)
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    temperature=0
)

def detect_intent(message: str):
    try:
        response = llm.invoke(
            f"""
You are an intent classifier for a SaaS chatbot.

Classify the user message into exactly ONE of:
- casual_greeting
- product_or_pricing
- high_intent_lead

Return ONLY valid JSON:
{{
  "intent": "<label>",
  "confidence": <number>
}}

User message: {message}
"""
        )

        result = json.loads(response.content)
        return result["intent"], result["confidence"]

    except Exception:
        # Heuristic fallback
        msg = message.lower()

        # High intent first
        if any(word in msg for word in [
            "i want", "buy", "try", "subscribe", "sign up", "signup",
            "pro plan", "youtube", "instagram", "ready"
        ]):
            return "high_intent_lead", 0.9

        # Pricing intent
        if any(word in msg for word in [
            "price", "pricing", "cost", "plan", "plans", "features"
        ]):
            return "product_or_pricing", 0.8

        return "casual_greeting", 0.7
