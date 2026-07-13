# ☀️ MerchantMind AI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-purple)
![Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-orange)
![Status](https://img.shields.io/badge/Status-Alpha-yellow)

> An Agentic AI Business Manager for Small Businesses.

MerchantMind AI is a multi-agent AI platform that helps small businesses make smarter business decisions through autonomous AI agents.

Instead of acting as a chatbot, MerchantMind AI coordinates multiple specialized AI agents that analyze different aspects of a business and produce actionable insights.

---

## 🌍 Problem

Small businesses often lack access to expensive business consultants, analysts, and marketing experts.

MerchantMind AI aims to bridge this gap by providing an AI-powered business manager capable of analyzing customer feedback, sales, inventory, and overall business performance.

---

## 🎯 Vision

Build an AI operating system for small businesses where multiple AI agents collaborate to improve business growth.

Target businesses include:

- ☕ Cafés
- 🍕 Restaurants
- 🥐 Bakeries
- 🏋️ Gyms
- 💇 Salons
- 🛒 Retail Stores
- 🩺 Clinics
- 📚 Bookstores
- 🔧 Repair Shops

---

# 🚀 Current Features

- ✅ FastAPI Backend
- ✅ LangGraph Multi-Agent Workflow
- ✅ Google Gemini Integration
- ✅ google-genai SDK
- ✅ Customer Review Analysis Agent
- ✅ Sales Analysis Agent
- ✅ Inventory Analysis Agent
- ✅ Structured AI Business Insights
- ✅ Modular Agent Architecture
- ✅ Jinja2 Prompt Templates
- ✅ Centralized LLM Service
- ✅ Logging & Exception Handling

---

# 🔄 Current Workflow
The multi-agent pipeline currently runs as:

Chief Business Officer
        ↓
    Review Agent
        ↓
    Sales Agent
        ↓
   Inventory Agent
        ↓
       END

**Official Demo Business:**
- Sunrise Café

**Demo Datasets:**
- reviews.json
- sales.csv (300 rows)
- inventory.csv (80 items)

---

# 🤖 AI Agents

✅ Completed
- Customer Review Agent
- Sales Analysis Agent
- Inventory Analysis Agent

🚧 In Progress
- Marketing Agent
- Business Strategy Agent
- Executive Report Agent

📝 Planned
- Competitor Intelligence Agent
- Finance Agent
---

# 🏗️ Tech Stack

## Backend

- Python
- FastAPI
- LangGraph
- Google Gemini API
- google-genai SDK
- Jinja2
- python-dotenv

## Database (Planned)

- PostgreSQL
- Redis

## Frontend (Planned)

- React

## DevOps (Planned)

- Docker
- GitHub Actions

## Others (Planned)
- Authentication
- Multi-business Support

---

# 📂 Project Structure

```text
MerchantMindAI/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── graph/
│   │   ├── prompts/
│   │   ├── services/
│   │   ├── tools/
│   │   └── ...
│   │
│   ├── sample_data/
│   └── tests/
│
├── frontend/        # Planned
└── development/     # Local planning (not tracked)
```

---

# 🎯 Current Status

MerchantMind AI currently supports AI-powered analysis of customer reviews, sales, and inventory through a coordinated multi-agent workflow, demonstrated on the Sunrise Café dataset.

Upcoming milestones include:

- Marketing Agent
- Business Strategy Agent
- Executive Business Report
- Business Performance Dashboard

---

# 📌 Project Status

🚧 Active Development (Alpha)

Current Version:

**v0.3.0-alpha.1**

---

# 👨‍💻 Author

Developed by **Sudarshan Upadhyay**

Project: **MerchantMind AI**

Built as part of an IBM Agentic AI & Automation Workshop while being designed as the foundation for a future SaaS startup.

