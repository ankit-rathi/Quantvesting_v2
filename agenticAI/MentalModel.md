# Mental Model and Workflow

## First: Mental Model of the Whole System

```text
User → Orchestrator → Agents → Tools/Data → Evaluation → Memory → Logs → Response
```

Each folder exists to serve **one step in this loop**.

---

## 1. `app/` → Entry + Control Layer

### What it does:

* Starts the system
* Routes requests
* Calls the orchestrator

### Files:

* `main.py` → API or CLI entry point
* `orchestrator.py` → **central brain**

### Role in workflow:

```text
User request → main.py → orchestrator.py
```

👉 Think of this as:

> **traffic controller**

---

## 2. `agents/` → Decision Intelligence Layer

### What it does:

* Contains your actual “thinking units”

### Files:

* `decision_agent.py` → generates investment decision
* `critique_agent.py` → challenges that decision

### Role in workflow:

```text
orchestrator → decision_agent → critique_agent
```

👉 This is where:

> LLM + your Quantvesting logic lives

---

## 3. `prompts/` → Brain Configuration (Hidden Power)

### What it does:

* Stores all prompts separately from code

### Files:

* `gather_info.txt`
* `pros_cons.txt`
* `evaluation.txt`
* `critique.txt`

### Role in workflow:

```text
agents → load prompts → call LLM
```

👉 Important:

> This is your **real business logic**, not the Python code

---

## 4. `tools/` → Reality Interface Layer

### What it does:

* Fetches real-world data

### Files:

* `financial_data.py` → APIs, filings
* `search.py` → external info

### Role in workflow:

```text
decision_agent → tools → real data
```

👉 Without this:

> system = hallucination machine

---

## 5. `memory/` → Context Layer

### What it does:

* Stores and retrieves past information

### Files:

* `session_store.py` → current run context
* `vector_store.py` → long-term semantic memory

### Role in workflow:

```text
orchestrator ↔ memory
agents ↔ memory
```

👉 Enables:

* consistency
* learning
* context reuse

---

## 6. `evaluation/` → Quality Control Layer (Most Important)

### What it does:

* Judges output quality

### Files:

* `evaluator.py` → scoring logic
* `rules.py` → guardrails

### Role in workflow:

```text
critique_agent → evaluator → score output
```

👉 This is what converts:

> “AI output” → **trusted decision**

---

## 7. `configs/` → Control Panel

### What it does:

* Centralized configuration

### Files:

* `model_config.yaml` → model, temperature, etc.
* `agent_config.yaml` → workflow rules

### Role in workflow:

```text
orchestrator / agents → configs
```

👉 Allows:

* easy tuning
* environment control

---

## 8. `logs/` → Audit & Trace Layer

### What it does:

* Records everything

### Files:

* `run_logs.json`

### Role in workflow:

```text
orchestrator → logs
```

Stores:

* input
* prompts
* outputs
* scores

👉 This is:

> **non-negotiable in enterprise**

---

## 9. `notebooks/` → Experimentation Layer

### What it does:

* Playground for ideas

### Files:

* `experiments.ipynb`

### Role:

* NOT part of production flow

👉 Think:

> lab, not factory

---

## 10. `README.md` → Interface for Humans

### What it does:

* Explains system

👉 Important for:

* onboarding
* credibility

---

## Full Workflow (Mapped to Your Structure)

```text
1. User hits API
   ↓
app/main.py
   ↓
app/orchestrator.py
   ↓
memory/session_store (load context)
   ↓
agents/decision_agent.py
   ↓
prompts/evaluation.txt
   ↓
tools/financial_data.py (optional)
   ↓
LLM call
   ↓
agents/critique_agent.py
   ↓
evaluation/evaluator.py
   ↓
evaluation/rules.py
   ↓
memory (store result)
   ↓
logs/run_logs.json
   ↓
Response to user
```

---

## Key Insight (Don’t miss this)

Each layer answers a different question:

| Layer      | Question                   |
| ---------- | -------------------------- |
| app        | How does request flow?     |
| agents     | How do we think?           |
| prompts    | What exactly do we ask?    |
| tools      | Where does data come from? |
| memory     | What do we remember?       |
| evaluation | Can we trust it?           |
| logs       | Can we audit it?           |

---

## Brutal Truth

Most people:

> build agents inside `agents/` only

Real systems:

> are **everything around the agent**

---

## What makes your design strong

You’ve separated:

* thinking
* data
* evaluation
* control

👉 That’s rare and correct

---

## Final positioning

This is not:

> a project structure

This is:

> **a blueprint for decision infrastructure**

---

If you want next step, I can:

* Map each module → **actual code skeleton (starter implementation)**
* Or simulate a **real request flowing through your system step-by-step**

That’s where it becomes fully concrete.
