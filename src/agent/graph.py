from agent.intent import detect_intent
from agent.rag import retrieve_answer
from agent.tools import mock_lead_capture

def agent_step(state: dict) -> dict:
    user_message = state["messages"][-1].strip()

    # SLOT FILLING (ONLY if already in high-intent flow)
    if state.get("intent") == "high_intent_lead":
        if state.get("name") is None:
            state["name"] = user_message
            state["response"] = "Thanks! Please share your email address."
            return state

        if state.get("email") is None and "@" in user_message:
            state["email"] = user_message
            state["response"] = (
                "Which creator platform do you use? (YouTube, Instagram, etc.)"
            )
            return state

        if state.get("platform") is None:
            state["platform"] = user_message

    # INTENT DETECTION
    intent, confidence = detect_intent(user_message)
    state["intent"] = intent
    state["confidence"] = confidence

    # High-intent override
    msg = user_message.lower()
    if any(word in msg for word in [
        "i want", "buy", "try", "subscribe", "sign up",
        "pro plan", "youtube", "instagram"
    ]):
        intent = "high_intent_lead"
        confidence = max(confidence or 0, 0.9)
        state["intent"] = intent
        state["confidence"] = confidence

    # Greeting
    if intent == "casual_greeting":
        state["response"] = (
            "Hi! I can help you with AutoStream pricing, plans, or features."
        )
        return state

    # RAG pricing
    if intent == "product_or_pricing":
        state["response"] = retrieve_answer(user_message)
        return state

    # High-intent lead completion
    if intent == "high_intent_lead" and confidence >= 0.7:
        if state.get("name") is None:
            state["response"] = "Great! May I know your name?"
            return state

        if state.get("email") is None:
            state["response"] = "Thanks! Please share your email address."
            return state

        if state.get("platform") is None:
            state["response"] = (
                "Which creator platform do you use? (YouTube, Instagram, etc.)"
            )
            return state

        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["response"] = (
            "Thanks! Your details have been captured. Our team will reach out shortly."
        )
        return state

    # Fallback
    state["response"] = (
        "Let me know if you'd like help with pricing or getting started."
    )
    return state
