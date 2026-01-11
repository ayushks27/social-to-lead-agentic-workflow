🚀 AutoStream: Social-to-Lead Agentic Workflow
AutoStream is a GenAI-powered conversational agent designed to transform social interactions into qualified business leads. Unlike a standard FAQ bot, this agent uses Intent Classification, Retrieval-Augmented Generation (RAG), and Stateful Slot-Filling to guide users from initial curiosity to lead capture.

🧠 Core Capabilities
1. Hybrid Intent Identification
The agent classifies user messages into three distinct categories to determine the next logical step in the conversation:

Casual Greeting: Engagement and rapport building.

Product/Pricing Inquiry: Dynamic information retrieval via RAG.

High-Intent Lead: Activation of the lead-generation funnel.

Note: Uses a Hybrid Approach (Gemini 1.5 Flash + Keyword Heuristics) to ensure 100% uptime even during API rate limits.

2. RAG-Powered Knowledge Base
The agent retrieves product specifications and company policies from a structured local knowledge base, ensuring responses are always grounded in fact.

Basic Plan: $29/mo (10 videos, 720p).

Pro Plan: $79/mo (Unlimited, 4K, AI Captions).

Policies: 7-day refund window & 24/7 Pro support.

3. Stateful Lead Capture (Slot-Filling)
When a user exhibits "High Intent," the agent shifts into a lead-capture mode. It maintains an internal state to collect:

Name

Email

Creator Platform (e.g., YouTube, Instagram)

The backend tool mock_lead_capture is only triggered once all three slots are successfully filled.

🏗 Architecture & State Management
Why LangChain?
While many bots are hard-coded, AutoStream uses LangChain for a modular architecture. This allows for a clean separation between the "Brain" (LLM), the "Memory" (State), and the "Hands" (Tools).

State Handling
The system employs a persistent in-memory dictionary that tracks:

Conversation History: For context-aware responses.

Intent Scores: To pivot between chat and lead capture.

Entity Extraction: To remember your name or email across multiple turns.

🛠 Project Structure
Plaintext

autostream-agent/
├── src/
│   ├── agent/
│   │   ├── intent.py      # LLM + Heuristic intent logic
│   │   ├── rag.py         # Knowledge retrieval logic
│   │   ├── graph.py       # Workflow & state transitions
│   │   └── tools.py       # Mock lead capture execution
│   ├── data/
│   │   └── knowledge_base.json
│   └── main.py            # CLI entry point
├── .env                   # API Keys (ignored by git)
├── requirements.txt       # Dependencies
└── README.md
🚀 Getting Started
Prerequisites
Python 3.9+

Google Gemini API Key

Installation
Clone & Enter Directory:

Bash

git clone https://github.com/your-repo/autostream-agent.git
cd autostream-agent
Setup Environment:

Bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Configure API Key: Create a .env file in the root directory:

Code snippet

GOOGLE_API_KEY=your_gemini_api_key_here
Run the Agent:

Bash

python src/main.py
📱 Conceptual Deployment: WhatsApp
To move from CLI to production, the agent is designed to sit behind a Webhook.

Incoming: Message received via WhatsApp Business API (Twilio/Meta).

Processing: Backend passes the sender_id to our State Manager to resume the session.

Action: Agent performs RAG or collects the next lead "slot."

Outgoing: Response is pushed back to the user via the API.
