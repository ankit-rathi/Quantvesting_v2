# Quantvesting Decision Agent

A decision intelligence system that applies the Quantvesting framework to investment analysis using an agentic workflow.

---

## 🧠 Why This Exists

Most investment tools focus on data, models, or predictions.

This project focuses on **decision quality**.

It converts unstructured information into structured investment decisions through a repeatable system:

**Gather → Structure → Evaluate → Critique**

The goal is not to predict markets, but to improve how decisions are made.

---

## ⚙️ What This System Does

Given a company, the system:

1. Gathers relevant information  
2. Structures pros and cons  
3. Evaluates using the Quantvesting framework:
   - Management Quality  
   - Business Quality  
   - Valuation Discipline  
4. Critically reviews its own output  
5. Scores and logs the decision  

---

## 🧩 System Architecture

```

Input → Context → Decision → Critique → Evaluation → Logging

```

This is not a single prompt, but a controlled decision loop with explicit stages and feedback.

---

## 🏗 Project Structure

```

quantvesting-agent/

app/        → orchestration and API layer
agents/     → decision and critique logic
prompts/    → versioned prompt templates
tools/      → data integration layer
memory/     → context and state management
evaluation/ → scoring and guardrails
logs/       → audit trail
notebooks/  → experimentation (non-production)

````

---

## 🔄 Example Workflow

**Input:** `TCS`

- Gather company context  
- Generate pros/cons  
- Apply Quantvesting framework  
- Produce investment thesis  
- Critique assumptions  
- Score output  
- Log decision  

---

## 🚀 How to Run (MVP)

```bash
# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn app.main:app --reload
````

Test in browser:

```
http://localhost:8000/analyze?company=TCS
```

---

## 🧠 Key Design Principles

* Decisions > predictions
* Structure over intuition
* Explicit reasoning over hidden logic
* Self-critique as a core feature
* Evaluation and logging are mandatory

---

## ⚠️ Limitations

* Relies on LLM-generated analysis (not financial advice)
* Data layer is currently limited or simulated
* Evaluation metrics are heuristic and evolving

---

## 🔮 Future Work

* Integrate real financial data sources
* Improve evaluation with scoring models
* Add portfolio-level decision logic
* Introduce memory across decisions

---

## 👤 Author Note

This project is part of a broader effort to design decision systems that improve thinking in complex domains like investing and AI.

It also serves as a hands-on exploration of agentic AI beyond chat-based interfaces.

---

## 🎯 Final Thought

This project is not about building an AI agent.

It is about encoding a disciplined investment decision process into a repeatable system.

