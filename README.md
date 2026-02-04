AutoStream – Social-to-Lead Agentic Workflow

Overview

    - AutoStream is a production-style GenAI conversational agent designed to convert natural language conversations into qualified business leads for a fictional SaaS product offering automated video editing tools for content creators.
    - The system goes beyond question-answering by detecting user intent, retrieving product knowledge, maintaining conversational state, and safely triggering backend actions only when qualification criteria are met.
    - This project demonstrates agentic workflow design, Retrieval-Augmented Generation (RAG), and multi-turn state management, aligned with real-world conversational AI systems.

Key Capabilities

1. Intent Detection (Hybrid Approach)

        - User messages are classified into one of three intents:
        - Casual greeting
        - Product or pricing inquiry
        - High-intent lead (ready to sign up)

Implementation details:

    - Primary: LLM-based intent classification (Gemini 1.5 Flash)
    - Fallback: Rule-based heuristics for deterministic behavior during API unavailability

This hybrid strategy improves reliability and reflects production-grade fault tolerance.

2. Retrieval-Augmented Generation (RAG)

Product information is retrieved dynamically from an external knowledge base rather than being hard-coded.

Knowledge coverage includes:

Pricing plans (Basic / Pro)

    - Feature limits and capabilities
    - Support and refund policies

Design choice:
RAG ensures responses remain maintainable, auditable, and easily extensible as product information evolves.

3. Stateful Lead Qualification

The agent maintains an in-memory conversation state across multiple turns, enabling:

    - Progressive slot filling (name, email, platform)
    - Context retention across 5–6 interactions
    - Safe gating of backend tool execution
    - Backend actions are triggered only after all required information is collected, preventing premature or invalid lead creation.

4. Backend Tool Execution (Mocked)

A backend tool simulates lead capture:

    def mock_lead_capture(name, email, platform):
        print(f"Lead captured successfully: {name}, {email}, {platform}")


This mirrors real API invocation patterns without introducing external dependencies.

Architecture

    User Message
       ↓
    Intent Detection (LLM + Heuristics)
       ↓
    ┌─────────────────────────────┐
    │  Product Inquiry?           │───▶ RAG Knowledge Retrieval
    │  High Intent?               │───▶ Slot Filling & State Update
    └─────────────────────────────┘
       ↓
    Backend Tool Trigger (Validated)

Project Structure

    social-to-lead-agentic-workflow/
    │
    ├── data/
    │   └── knowledge_base.json        # Product plans, pricing & policy knowledge
    │
    ├── src/
    │   ├── agent/
    │   │   ├── intent.py              # Hybrid intent classification
    │   │   ├── rag.py                 # Retrieval-Augmented Generation logic
    │   │   ├── tools.py               # Backend tools (lead capture)
    │   │   ├── graph.py               # Agent orchestration & state handling
    │   │
    │   └── main.py                    # Application entry point
    │
    ├── leads.csv                      # Mock persistence for captured leads
    ├── .env
    ├── requirements.txt
    ├── README.md
    └── LICENSE

Design Rationale

    - Modular agent components for testability and maintainability
    - Explicit state management for multi-turn conversations
    - Externalized knowledge base to support scalable RAG
    - Clear separation between reasoning, retrieval, and execution layers
    - This mirrors design patterns used in production conversational AI systems.

Local Setup

Clone Repository

    git clone https://github.com/ayushks27/social-to-lead-agentic-workflow.git
    cd social-to-lead-agentic-workflow

Environment Setup

    python -m venv venv
    source venv/bin/activate   # Windows: venv\Scripts\activate
    pip install -r requirements.txt

Configure Environment Variables

Create a .env file:

    GOOGLE_API_KEY=your_api_key_here

A heuristic fallback allows the agent to run even without API access.

    Run the Agent
    python src/main.py

Example Interaction

    User: Hi
    Agent: Hi! I can help you with AutoStream pricing, plans, or features.
    
    User: Tell me about pricing
    Agent: AutoStream offers:
    - Basic Plan: $29/month
    - Pro Plan: $79/month
    
    User: I want the Pro plan for my YouTube channel
    Agent: Great! May I know your name?
    
    User: Ayush
    Agent: Please share your email address.
    
    User: ayush@gmail.com
    Agent: Which creator platform do you use?
    
    User: YouTube
    Lead captured successfully: Ayush, ayush@gmail.com, YouTube

Deployment Considerations

The agent is designed to be deployed behind messaging platforms such as WhatsApp or web chat interfaces using webhook-based integrations. Conversation state and tool execution logic are platform-agnostic.

License

MIT License
