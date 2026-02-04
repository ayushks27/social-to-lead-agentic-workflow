AutoStream – Social-to-Lead Agentic Workflow

AutoStream is a GenAI-powered conversational agent designed to convert user conversations into qualified business leads, rather than functioning as a simple FAQ chatbot. The project simulates a real-world SaaS use case where conversational AI is used to identify intent, answer product questions, and safely trigger backend lead capture workflows. AutoStream is a fictional SaaS product offering automated video editing tools for content creators.

Problem Statement

Most conversational agents stop at answering user questions.
AutoStream goes further by:

    - Detecting high-intent users
    - Collecting lead information across multiple turns
    - Triggering backend actions only when qualification is complete

This mirrors real-world GenAI use cases in sales automation, growth engineering, and customer acquisition.

Agent Capabilities

1. Intent Identification
   
            - Each user message is classified into one of three intents:
            - Casual Greeting
            - Product / Pricing Inquiry
            - High-Intent Lead (ready to convert)
            - Hybrid Detection Strategy
            - Primary: LLM-based intent classification using Gemini 1.5 Flash
            - Fallback: Rule-based keyword heuristics
    
    This hybrid approach ensures:
    
        - Robust behavior during local testing
        - Graceful degradation when API access is unavailable
        - Production-like reliability

2. RAG-Powered Knowledge Retrieval

The agent uses Retrieval-Augmented Generation (RAG) with a local knowledge base (JSON / Markdown).

Included Knowledge Domains:

    Pricing Plans
    
    - Basic Plan — $29/month
    
        10 videos/month
        720p resolution
    
    - Pro Plan — $79/month
    
        Unlimited videos
        4K resolution
        AI captions
    
    - Company Policies
    
        No refunds after 7 days
        24/7 support available only on Pro plan
    
Responses are retrieved dynamically, not hard-coded, ensuring maintainability and extensibility.

3. Tool Execution – Lead Capture

When high intent is detected, the agent initiates a multi-turn lead qualification flow.

Lead Information Collected:

    Name
    Email

Creator platform (YouTube, Instagram, etc.)

Key Design Principles

    - Uses slot-filling to retain partial information
    - Maintains conversation state across turns
    - Backend tools are triggered only after all required fields are collected

Backend Tool (Mock Implementation)

    def mock_lead_capture(name, email, platform):
        print(f"Lead captured successfully: {name}, {email}, {platform}")

This prevents premature or invalid lead creation.

Project Structure

    social-to-lead-agentic-workflow/
    │
    ├── data/
    │   └── knowledge_base.json        # Product plans, pricing & policy knowledge (RAG source)
    │
    ├── src/
    │   ├── agent/
    │   │   ├── __init__.py
    │   │   ├── intent.py              # Hybrid intent detection (LLM + heuristics)
    │   │   ├── rag.py                 # Retrieval-Augmented Generation logic
    │   │   ├── tools.py               # Backend tools (mock lead capture)
    │   │   ├── graph.py               # Agent orchestration & state transitions
    │   │
    │   └── main.py                    # Application entry point
    │
    ├── leads.csv                      # Mock backend storage for captured leads
    ├── .env                           # Environment variables (API keys)
    ├── .gitignore
    ├── requirements.txt               # Project dependencies
    ├── README.md
    └── LICENSE

Architecture Overview

    Agent Architecture
    
        ```mermaid
        flowchart TD
            User[User Message]
            
            User --> Intent[Intent Detection]
            
            Intent -->|Greeting| Response[Conversational Response]
            Intent -->|Pricing / Product| RAG[RAG Knowledge Retrieval]
            Intent -->|High Intent| State[Lead Qualification State]
            
            RAG --> Response
            
            State --> SlotFill[Slot Filling]
            SlotFill -->|Missing Info| Response
            SlotFill -->|All Info Collected| Tool[Lead Capture Tool]
            
            Tool --> Backend[(Mock Backend / CSV)]
            Backend --> Response

Why LangChain?

The project uses LangChain to build a modular, agentic workflow rather than a rule-based chatbot.

LangChain enables:

    - Clear separation of concerns (intent, retrieval, tools)
    - Prompt modularity
    - Deterministic tool execution

Although LangGraph is preferred in some production systems, this implementation uses explicit state handling in LangChain, which is:

    - Simpler
    - Stable
    - Fully compliant with the assignment requirements

State Management

The agent maintains an in-memory state dictionary across conversation turns.

State Tracks:

    - Conversation history
    - Detected intent and confidence
    - Partially collected lead details (name, email, platform)

During high-intent flows, the agent incrementally updates state using slot-filling logic.
This approach is functionally equivalent to LangGraph memory nodes and demonstrates clean, real-world state management.

Enhancement: Hybrid Intent Detection

    - To increase robustness, the agent combines:
    - LLM-based classification (Gemini 1.5 Flash)
    - Rule-based heuristics as a fallback

This reflects real-world conversational AI system design, where systems must remain functional even during partial outages or API failures.

Running the Project Locally

1. Clone the Repository

        git clone https://github.com/ayushks27/social-to-lead-agentic-workflow.git
        cd social-to-lead-agentic-workflow

3. Create a Virtual Environment
   
        python -m venv venv
        source venv/bin/activate   # Windows: venv\Scripts\activate

4. Install Dependencies
   
        pip install -r requirements.txt

5. Set Environment Variables

Create a .env file:

    GOOGLE_API_KEY=your_api_key_here

Note: The agent is configured for Gemini 1.5 Flash as required.
A heuristic fallback allows the project to run even without API access.

5. Run the Agent
   
        python src/main.py

Sample Conversation Flow:

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

WhatsApp Deployment (Conceptual Design):

AutoStream can be deployed on WhatsApp using a Webhook-based architecture via the WhatsApp Business API (Meta / Twilio).

    - High-Level Flow
    
    - Incoming Message
      User message triggers a backend webhook.
    
    - Agent Processing
    Message is passed to the AutoStream agent for intent detection, RAG, or lead qualification.
    
    - Response Generation
    Agent responds based on conversation state.
    
    - Message Delivery
    Response is sent back via WhatsApp Business API.

This design enables scalable, real-time social-to-lead conversion while preserving conversational context.

Summary:

AutoStream demonstrates:

    - Agentic conversational design
    - Hybrid intent detection
    - RAG-based knowledge retrieval
    - Safe, stateful tool execution
    - Production-oriented architecture decisions

This project reflects real-world GenAI system design used in sales automation and conversational growth platforms.

Author 

    Purnendu Raghav Srivastava
