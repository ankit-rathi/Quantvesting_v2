# Quantvesting Decision Agent

A decision intelligence system that applies the Quantvesting framework to investment analysis. The agent transforms unstructured information into structured insights, evaluates opportunities across key dimensions, and produces a reasoned investment view through an iterative decision loop.

## 1. How to Structure This in Google Colab

You’re not building a repo first—you’re building a **working system notebook**.

Create a new notebook:

**`quantvesting_agent.ipynb`**

Structure it like this:

---

### Cell 1 — Install dependencies

```python
!pip install openai python-dotenv
```

---

### Cell 2 — Setup API key (Colab way)

Avoid `.env` in Colab. Use:

```python
import os

os.environ["OPENAI_API_KEY"] = "your_api_key_here"
```

👉 Later you can move to `.env` locally.

---

### Cell 3 — LLM wrapper

```python
from openai import OpenAI

client = OpenAI()

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

---

## 2. Build Agent Step-by-Step (separate cells)

### Cell 4 — Gather Info

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

---

### Cell 5 — Pros & Cons

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

---

### Cell 6 — Evaluation

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

---

### Cell 7 — Agent Loop

```python
def decision_agent(company):
    print("Gathering info...")
    info = gather_info(company)

    print("Analyzing pros/cons...")
    pros_cons = analyze_pros_cons(info)

    print("Evaluating...")
    decision = evaluate_investment(pros_cons)

    return decision
```

---

### Cell 8 — Run it

```python
result = decision_agent("TCS")
print(result)
```

---

## 3. Make It Interactive (High ROI)

Instead of hardcoding:

```python
company = input("Enter company name: ")
result = decision_agent(company)
print(result)
```

👉 Now it becomes a usable tool.

---

## 4. Add Self-Critique (this is where learning jumps)

## Cell 9 — Improve Agent

```python
def refine_decision(company):
    decision = decision_agent(company)

    review_prompt = f"""
    Critically review this investment decision:

    {decision}

    Identify flaws, missing risks, and biases.
    """

    review = ask_llm(review_prompt)

    return decision, review
```

---

### Cell 10 — Run refinement

```python
decision, review = refine_decision("TCS")

print("Decision:\n", decision)
print("\nReview:\n", review)
```

---

## 5. Save Outputs (memory)

```python
with open("history.txt", "a") as f:
    f.write(decision + "\n\n" + review + "\n\n")
```

👉 Download from Colab if needed.

---

## 6. Upgrade to Quantvesting Logic (critical)

Modify evaluation prompt:

```python
def evaluate_investment(pros_cons):
    prompt = f"""
    Based on the following analysis:

    {pros_cons}

    Evaluate using:
    - Management Quality
    - Business Quality
    - Valuation Discipline

    Provide:
    - Investment thesis
    - Key risks
    - Final recommendation
    """
    return ask_llm(prompt)
```

👉 Now it aligns with your framework.

---

## 7. Connect to GitHub

In Colab:

* File → Save a copy in GitHub
* Or download `.ipynb` → push manually

👉 Keep:

* Notebook (execution)
* README (your explanation)

---

## 8. Common mistakes in Colab (avoid these)

* ❌ Running everything in one cell
* ❌ Not separating logic (hard to debug)
* ❌ Overengineering too early
* ❌ Adding APIs before mastering flow

---

## What you’re actually learning

Not “how to use OpenAI”

But:

```text
Decision System Design
+
Agent Loop Thinking
+
Prompt as Control Logic
```

---

## When to move beyond Colab

Only after:

* You understand failure cases
* You improve outputs intentionally
* You want persistence + scale

Then move to:

* Python scripts
* GitHub repo
* Later → Kiro

---

## Final advice

Don’t treat this as:

> “build an AI project”

Treat it as:

> **encode your investment thinking into a system**

---

If you want next step, I can:

* Convert this into a **clean GitHub-ready project structure**
* Or help you build **real financial data integration (Screener, APIs, filings)**

That’s where it becomes genuinely powerful.


That’s where this becomes genuinely powerful.
