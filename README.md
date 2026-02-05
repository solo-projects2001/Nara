# Nara — Offline Meta-System for Deterministic System Generation

Nara is a **standalone Meta-System** operating at the **control layer**, not the task layer.

It does **not** directly solve end-user problems.
Instead, it **designs, executes, evaluates, and repairs** other systems:

- pipelines
- tools
- workflows
- multi-component project skeletons

All locally, offline, and auditable.

---

## What Nara Is

A **Meta-System** is a system that:

- converts intent → structured system design
- generates inspectable artifacts (not hidden outputs)
- executes locally inside bounded environments
- detects failures deterministically
- applies targeted repairs (non-blind)
- stops safely (no infinite loops)

Nara is built to be:

- deterministic
- offline-first
- enterprise-auditable
- contract-driven
- repair-bounded

---

## Core Capabilities

### Intent → Structure Synthesis
High-level goals become structured designs:

- system type inference
- blueprint selection
- component decomposition
- execution graph planning

### Artifact-Centric Generation
Every run produces a full inspectable project skeleton:

- `system_spec.json`
- `blueprint.json`
- `contracts.json`
- `executor_plan.json`
- workspace components

No magic memory. No hidden state.

### Local Execution + Metrics
Generated systems run locally:

- stdout/stderr captured
- exit codes recorded
- logs emitted

### Failure Detection + Classification
Failures are classified deterministically:

- syntax errors
- runtime failures
- contract mismatches
- domain violations

### Targeted Repair
Repairs modify only the failing component:

- preserves unaffected artifacts
- bounded retry budget
- stops on irreparable failure

### Explainability + Observability
Every decision is logged:

- intent
- plan
- artifacts
- execution results
- repair actions

---
## Run

Setup:

```bash
python setup_nara.py
