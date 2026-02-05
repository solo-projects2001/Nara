# NARA — META-SYSTEM SPECIFICATION

## Definition
Nara is a standalone Meta-System operating strictly at the control layer.

It does NOT solve end-user tasks.
It designs, executes, evaluates, and repairs other systems.

## Core Guarantees
- Deterministic behavior
- Offline-only execution
- No cloud services
- No paid APIs
- No hidden state
- No autonomous self-expansion
- Explicit stop conditions

## Scope
IN SCOPE:
- System design
- Pipeline synthesis
- Artifact generation
- Local execution
- Failure classification
- Targeted repair
- Explainability

OUT OF SCOPE:
- Chatbot UX
- End-user product features
- General intelligence
- Long-running autonomous agents
- Cloud inference

## Safety Rules
- Stop on ambiguity
- Reject unsafe or forbidden intents
- Never guess execution domains
- Never self-modify Nara

## Finality
This document freezes Nara’s definition.
Any change requires a new spec version.
