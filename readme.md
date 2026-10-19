# 🤖 Multi-Agent AI Workflows with LangChain & Groq

A collection of sequential **Multi-Agent AI Systems** built in Python using **LangChain (`langchain-groq`)** and powered by the **`openai/gpt-oss-120b`** model on **Groq**. 

Each script demonstrates how specialized AI agents can collaborate in a chained pipeline—passing context, research, critiques, and structured outputs from one agent to the next to solve complex real-world tasks.

---

## 📂 Project Architecture & Pipelines

This repository contains four distinct multi-agent pipelines progressing from 2-agent systems to 4-agent workflows:

### 1. Two-Agent Research & Review System (`multisystem.py`)
A foundational two-step verification pipeline for rapid topic research:
* **Agent 1 (`research_agent`)**: Generates a concise (<500 words) research summary complete with real-life examples and references.
* **Agent 2 (`review_agent`)**: Audits the initial output, summarizes key findings, highlights strengths and weaknesses, and suggests improvements.

### 2. Three-Agent Editorial Publishing Pipeline (`Threesystemagent.py`)
An automated research-to-publication editorial workflow:
* **Step 1 — Writer Agent (`writer_agent`)**: Produces a structured 350–500 word analytical draft with an executive overview, core mechanisms, named case studies, and industry references.
* **Step 2 — Reviewer Agent (`reviewer_agent`)**: Acts as a senior peer reviewer to evaluate accuracy, logical flow, and blind spots, outputting numbered actionable directives without rewriting the draft.
* **Step 3 — Editor Agent (`editor_agent`)**: Synthesizes the original draft and reviewer directives into a polished, Markdown-formatted final article with an editorial change summary.

### 3. Four-Agent Smart Shopping Advisor (`agents.py`)
An end-to-end e-commerce product discovery and purchasing decision pipeline:
* **Agent 1 — Product Search (`product_search_agent`)**: Identifies 2–3 specific real-world product models matching the user's query and target budget.
* **Agent 2 — Price & Budget Analyst (`price_budget_analyst`)**: Evaluates budget fit, value-for-money metrics, and hidden ownership/maintenance costs.
* **Agent 3 — Review Analyst (`review_analyst`)**: Audits long-term consumer sentiment, recurring praises, common pain points, and reliability risks (Low/Medium/High).
* **Agent 4 — Recommendation Analyst (`recommendation_analyst`)**: Synthesizes all prior analyses into a ranked hierarchy (1st Place, Runner-Up, Alternative) with clear *"Buy If / Skip If"* rules.

### 4. Four-Agent End-to-End Travel Planner (`Travel.py`)
A comprehensive travel itinerary and financial auditing pipeline:
* **Agent 1 — Destination Researcher (`destination_researcher`)**: Curates 6–8 geographically grouped attractions with entry fees and optimal visiting windows.
* **Agent 2 — Budget Planner (`budget_planner`)**: Calculates category-wise costs (Stay, Food, Local Transport, Sightseeing, and a 10% Contingency Buffer) against the user's target budget.
* **Agent 3 — Itinerary Planner (`itinerary_planner`)**: Builds a geographically logical day-by-day schedule broken into Morning, Afternoon, and Evening slots.
* **Agent 4 — Travel Reviewer (`travel_reviewer`)**: Audits pacing realism, budget feasibility, local scam warnings, advance booking alerts, and cultural etiquette before issuing a final approval verdict.

---

## 🛠️ Tech Stack

* **Language:** Python 3.9+
* **Framework:** [LangChain](https://www.langchain.com/) (`langchain-groq`)
* **LLM Inference:** [Groq Cloud API](https://console.groq.com/) (`openai/gpt-oss-120b`)
* **Environment Management:** `python-dotenv`

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure Your Environment Variables
Create a `.env` file in the project root directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 💻 Usage

Run any of the multi-agent pipelines directly from the terminal:

```bash
# Run the 2-Agent Research & Review pipeline
python multisystem.py

# Run the 3-Agent Writer -> Reviewer -> Editor pipeline
python Threesystemagent.py

# Run the 4-Agent Product Shopping Advisor
python agents.py

# Run the 4-Agent Travel & Budget Planner (supports custom input or default Udaipur trip)
python Travel.py
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).