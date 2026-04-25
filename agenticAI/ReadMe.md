# Quantvesting Decision Agent

A decision intelligence system that applies the Quantvesting framework to investment analysis. The agent transforms unstructured information into structured insights, evaluates opportunities across key dimensions, and produces a reasoned investment view through an iterative decision loop.

## ⚙️ 0. Setup (keep it simple)

### Environment

* Python 3.10+
* Editor: VS Code (or anything basic)
* No frameworks

### Install only this:

```bash
pip install openai python-dotenv
```

### Create `.env`

```bash
OPENAI_API_KEY=your_key_here
```

---

## 🧠 1. Define the Agent (before coding)

Your agent is:

```text
Goal: Evaluate an investment
Steps:
1. Gather info
2. Structure pros/cons
3. Evaluate decision
```

👉 This clarity matters more than code.

---

## 🧱 2. Basic LLM Call (foundation)

```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

---

## 🔍 3. Step 1 — Gather Information

Start simple: simulate research via prompt (don’t overcomplicate with APIs yet)

```python
def gather_info(company):
    prompt = f"""
    Provide a structured overview of {company}:
    - Business model
    - Revenue drivers
    - Risks
    - Industry trends
    """
    return ask_llm(prompt)
```

👉 Concept learned:

* LLM as **research synthesizer**

---

## ⚖️ 4. Step 2 — Pros & Cons

```python
def analyze_pros_cons(info):
    prompt = f"""
    Based on the following information:

    {info}

    List:
    Pros:
    Cons:
    """
    return ask_llm(prompt)
```

👉 Concept:

* Structuring unstructured data

---

## 🧮 5. Step 3 — Evaluation (Decision Layer)

```python
def evaluate_investment(pros_cons):
    prompt = f"""
    Based on the following analysis:

    {pros_cons}

    Provide:
    - Investment thesis
    - Risks
    - Final recommendation (Buy / Avoid / Watch)
    - Confidence level (Low/Medium/High)
    """
    return ask_llm(prompt)
```

👉 Concept:

* Decision synthesis

---

## 🔁 6. Connect Everything (your first “agent”)

```python
def decision_agent(company):
    print("Gathering info...")
    info = gather_info(company)

    print("Analyzing pros/cons...")
    pros_cons = analyze_pros_cons(info)

    print("Evaluating...")
    decision = evaluate_investment(pros_cons)

    return decision


if __name__ == "__main__":
    result = decision_agent("TCS")
    print("\nFinal Output:\n")
    print(result)
```

---

## 🧠 What you just built

Not a toy.

You built:

```text
Input → Research → Structure → Evaluate → Output
```

👉 This is a **decision system**

---

## ⚠️ Now improve it (this is where learning happens)

### 1. Add iteration (real agent behavior)

```python
def refine_decision(company):
    decision = decision_agent(company)

    review_prompt = f"""
    Critically review this investment decision:

    {decision}

    Identify flaws and suggest improvements.
    """

    review = ask_llm(review_prompt)

    return decision, review
```

👉 Concept:

* Self-critique loop

---

### 2. Add constraints (your Quantvesting lens)

Modify prompt:

```text
Evaluate based on:
- Management quality
- Business quality
- Valuation discipline
```

👉 Now it becomes YOUR system

---

### 3. Add memory (simple version)

Save outputs to file:

```python
with open("history.txt", "a") as f:
    f.write(result + "\n\n")
```

👉 Concept:

* Persistence

---

## 🚀 When to move forward

Only after you:

* understand each step
* can debug bad outputs
* can improve prompts intentionally

---

## 🔄 Then introduce tools (next step)

* Add real data (APIs, filings)
* Add scoring system
* Add multi-step reasoning

---

## 🎯 Where Kiro fits (later)

After this, tools like Kiro will:

* orchestrate these steps
* manage workflows
* scale agents

---

## 🔥 Final truth

Right now:

> You are building a **thinking system**

Not:

> a chatbot

---

## 🧭 If you want next step

I can:

* Upgrade this into a **Quantvesting-grade decision agent**
* Add **real financial data integration**
* Or help you convert this into your **ContextOS AI system**

That’s where this becomes genuinely powerful.
