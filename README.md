# Agentic-AI

> Hands-on notebooks and utilities for building AI agents with **LangChain**, **LangGraph**, and **RAG** workflows in Python.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/LangChain-Agent%20Workflows-1C3C3C" alt="LangChain" />
  <img src="https://img.shields.io/badge/LangGraph-Stateful%20Agents-4B32C3" alt="LangGraph" />
  <img src="https://img.shields.io/badge/Pinecone-Vector%20DB-0F6FFF" alt="Pinecone" />
  <img src="https://img.shields.io/badge/Playwright-PDF%20Automation-2EAD33?logo=playwright&logoColor=white" alt="Playwright" />
</p>

## Overview

This repository is a learning-and-building workspace for agentic AI patterns. It includes notebook-based experiments across:

- LangChain basics, tools, messages, structured output, and middleware
- LangGraph stateful chatbot flows
- RAG experiments with PDF ingestion and Pinecone-backed vector retrieval
- Early LLM security/guardrails exploration
- A Python utility to export ChatGPT shared conversations to PDFs

## Key Topics Covered

- **LLM integrations** (Google GenAI, Groq)
- **Agent tooling** and function/tool calling
- **RAG pipelines** with embedding + retrieval patterns
- **Vector storage** with Pinecone
- **Notebook-driven prototyping** for rapid iteration

## Project Structure

| Path | Purpose |
|---|---|
| `/langchain` | Core LangChain notebooks (`01`–`05`) for fundamentals and agent workflows |
| `/langgraph` | LangGraph notebook examples for chatbot and state handling |
| `/RAG` | RAG notebooks, including retrieval and vector database usage |
| `/llm Security` | Guardrails/security exploration notebook |
| `/pdfs` | Generated or sample PDF assets |
| `/chatgpt_to_pdf.py` | Playwright-based script to convert ChatGPT shared links into PDFs |
| `/requirements.txt` | Pip-friendly dependency list |
| `/pyproject.toml` | Project metadata and Python dependency definitions |

## Setup

### 1) Clone and enter the project

```bash
git clone https://github.com/pratikadamas/Agentic-AI.git
cd Agentic-AI
```

### 2) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows PowerShell
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Several notebooks load credentials from a `.env` file via `python-dotenv`.

Create `.env` in the repository root with only the keys you need:

```env
GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
PINECONE_API_KEY=your_pinecone_key
```

> Keep secrets local. `.env` files are ignored by git in this repository.

## Getting Started

- Open notebooks with Jupyter or VS Code.
- Suggested order for beginners:
  1. `/langchain/01-langchainIntro.ipynb`
  2. `/langchain/02-tools.ipynb`
  3. `/langgraph/01basicchatbot.ipynb`
  4. `/RAG/01intro.ipynb`

Run Jupyter locally:

```bash
jupyter notebook
```

## Utility Script: ChatGPT to PDF

The script `chatgpt_to_pdf.py` converts configured ChatGPT share URLs into PDF files saved under `pdfs/`.

```bash
python chatgpt_to_pdf.py
```

## Contributing

Contributions are welcome through issues and pull requests.

## License

This repository currently does **not** include a license file.
