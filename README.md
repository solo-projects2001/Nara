# Nara Meta-System

Nara is a **control-layer Meta-System**, not an end-user chatbot.

It designs, executes, validates, and repairs other systems locally.

## Guarantees

- Offline-first (Ollama only)
- Deterministic artifact generation
- Inspectable pipelines (`design/pipeline.json`)
- Targeted repair (bounded patches)
- Human-auditable logs

## Run

Setup:

```bash
python setup_nara.py
