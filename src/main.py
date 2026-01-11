import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

from agent.graph import agent_step

state = {
    "messages": [],
    "intent": None,
    "confidence": None,
    "name": None,
    "email": None,
    "platform": None,
    "response": None
}

print("AutoStream Agent (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Persist conversation memory
    state["messages"].append(user_input)

    result = agent_step(state)

    print("Agent:", result["response"], "\n")

    # Persist state across turns
    state.update({
        "intent": result.get("intent"),
        "confidence": result.get("confidence"),
        "name": result.get("name"),
        "email": result.get("email"),
        "platform": result.get("platform"),
        "response": result.get("response"),
    })
