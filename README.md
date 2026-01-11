AutoStream – Social-to-Lead Agentic Workflow

This project implements a GenAI-powered conversational agent for a fictional SaaS product AutoStream.

AutoStream provides automated video editing tools for content creators. The goal of this agent is to convert conversational interactions into qualified business leads, not just answer user queries.

The agent is designed to:

    -Understand user intent
    
    -Answer product and pricing questions accurately
    
    -Identify high-intent users
    
    -Trigger backend lead capture actions safely


🧠 Agent Capabilities

1️. Intent Identification

The agent classifies user messages into three intents:

    -Casual Greeting
    
    -Product or Pricing Inquiry
    
    -High-Intent Lead (ready to sign up)
    
    
Intent detection uses a hybrid approach:
    
    -Primary: LLM-based classification using Gemini 1.5 Flash
    
    -Fallback: Rule-based heuristics for reliability during local testing or API unavailability

2️. RAG-Powered Knowledge Retrieval

The agent uses Retrieval-Augmented Generation (RAG) with a local knowledge base (JSON/Markdown).

    -Included Knowledge
    
    -Basic Plan
    
    -$29/month
    
    -10 videos/month
    
    -720p resolution
    
    -Pro Plan
    
    $79/month
    
    -Unlimited videos
    
    -4K resolution
    
    -AI captions
    
    -Company Policies
    
    -No refunds after 7 days
    
    -24/7 support available only on Pro plan
    
Responses are retrieved dynamically from the knowledge base, not hard-coded.

3️. Tool Execution – Lead Capture

When a user shows high intent, the agent:

Collects the following details across multiple turns:

    -Name
    
    -Email
    
    -Creator platform (YouTube, Instagram, etc.)
    
    -Uses slot-filling to retain partially collected data
    
    -Triggers the backend tool only after all details are collected

    def mock_lead_capture(name, email, platform):
        print(f"Lead captured successfully: {name}, {email}, {platform}")

The tool is never triggered prematurely.


🔧 Architecture Explanation

Why LangChain

This project uses LangChain to build a modular, agentic conversational workflow instead of a simple rule-based chatbot. LangChain provides structured abstractions for working with Large Language Models, prompt handling, and tool execution, making it suitable for real-world GenAI applications like Inflx. The framework allows clear separation between intent detection, RAG-based knowledge retrieval, and backend tool execution. Although LangGraph is preferred, the assignment explicitly allows equivalent approaches, and this implementation uses LangChain with explicit state handling to achieve the same outcome in a simpler and more stable manner.

State Management

The agent maintains a persistent in-memory state dictionary across conversation turns, enabling memory retention over 5–6 interactions. The state stores conversation history, detected intent, confidence scores, and partially collected lead details (name, email, platform). During high-intent flows, the agent uses a slot-filling approach to incrementally update this state based on user responses. This ensures context continuity and guarantees that backend actions are triggered only when all required information is present. This approach is functionally equivalent to LangGraph state or memory buffers and demonstrates clean, real-world state management.


⭐ Enhancement: Hybrid Intent Detection (LLM + Heuristics)

To improve robustness, the agent uses a hybrid intent detection strategy:

    -Primary: Gemini 1.5 Flash for intent classification
    
    -Fallback: Keyword-based heuristics when LLM access is unavailable

This ensures reliable behavior during local testing, demos, and production-like failures, and reflects real-world conversational AI system design.

How to Run the Project Locally

-> Clone the Repository

    git clone <your-github-repo-url>
    cd autostream-agent

-> Create a Virtual Environment

    python -m venv venv
    source venv/bin/activate   # Windows: venv\Scripts\activate

-> Install Dependencies

    pip install -r requirements.txt

Set Environment Variables

Create a .env file:

    GOOGLE_API_KEY=your_api_key_here

Note: The agent is configured for Gemini 1.5 Flash as required by the assignment.
A heuristic fallback ensures local execution even if API access is unavailable.

-> Run the Agent

    python src/main.py

💬 Sample Conversation Flow

    User: Hi
    Agent: Hi! I can help you with AutoStream pricing, plans, or features.
    
    User: Tell me about pricing
    Agent: AutoStream Pricing:
    - Basic Plan: $29/month...
    - Pro Plan: $79/month...
    
    User: I want the Pro plan for my YouTube channel
    Agent: Great! May I know your name?
    
    User: Ayush
    Agent: Thanks! Please share your email address.
    
    User: ayush@gmail.com
    Agent: Which creator platform do you use?
    
    User: YouTube
    Lead captured successfully: Ayush, ayush@gmail.com, YouTube
    Agent: Thanks! Your details have been captured. Our team will reach out shortly.


📲 WhatsApp Deployment (Conceptual Design)

To deploy this agent on WhatsApp, a Webhook-based integration can be implemented using the WhatsApp Business API (via Meta or providers like Twilio).

    -Incoming Message
    A user message triggers a webhook on the backend containing sender ID and message text.
    
    -Agent Processing
    The backend forwards the message to the AutoStream agent, which updates state, detects intent, performs RAG, or continues lead qualification.
    
    -Response Generation
    The agent generates a response based on the current conversation state.
    
    -Sending Reply
    The backend sends the response back to the user using the WhatsApp Business API.

This architecture enables scalable, real-time social-to-lead conversion while preserving conversational context.


📁 Project Structure
src/
 ├── agent/
 │   ├── intent.py        # Intent detection (LLM + heuristics)
 │   ├── rag.py           # RAG knowledge retrieval
 │   ├── graph.py         # Agent logic & state transitions
 │   ├── tools.py         # Mock lead capture tool
 ├── data/
 │   └── knowledge_base.json
 └── main.py              # Application entry point
