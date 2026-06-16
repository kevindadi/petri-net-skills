---
name: petri-net-explainer
description: Explain Petri nets from text descriptions, simple structured definitions, markings, or Petri-net artifacts. Use when Codex needs to describe the meaning of places, transitions, arcs, and markings; identify enabled transitions; explain firing effects step by step; summarize behavioral intuition; or walk a user through a small Petri-net model for teaching, analysis support, or model review.
---

# Petri Net Explainer

## Overview

Explain a small or medium Petri net in clear operational language. Favor structural explanation, firing intuition, and explicit assumptions over formal proof.

Treat this skill as an interpreter and walkthrough guide. Do not pretend it is a full verification engine.

## Input Modes

Handle these input styles:

1. A text description of places, transitions, arcs, and an initial marking.
2. A natural-language process description that implies a Petri net.
3. A partially specified model with only names and a few connections.
4. A request to explain a specific marking or a specific transition firing.

If the user provides a diagram or file but the structure is not machine-readable in the current context, explain what can be inferred and state what is still needed.

## Core Workflow

1. Extract the net elements that are actually given.
2. State the interpretation boundary:
   - Distinguish explicit facts from inferred semantics.
   - Say when place or transition names suggest business meaning.
3. Read the marking:
   - Explain what each token placement means operationally.
   - Identify enabled transitions only when preconditions are explicit.
4. Explain one-step behavior:
   - For each enabled transition, describe consumed tokens, produced tokens, and the resulting intuition.
5. Summarize the broader pattern:
   - Point out cycles, synchronization points, mutual exclusion, waiting states, or resource flow when visible.
6. List ambiguities and assumptions.

## Output Shape

Default to this structure unless the user asks for a different format:

1. `Overview`
   - One short paragraph on what the net appears to model.
2. `Elements`
   - Explain places, transitions, and any notable arcs.
3. `Current Marking`
   - Explain what the present state means.
4. `Enabled Transitions`
   - Name each enabled transition and why it is enabled.
5. `Possible Next Step`
   - Walk through one or more firings in plain language.
6. `Behavioral Notes`
   - Mention loops, bottlenecks, joins, splits, waiting, or deadlock risk signals.
7. `Assumptions`
   - Separate missing information from actual conclusions.

## Explanation Rules

- Prefer precise plain language over symbolic overload when the user is learning.
- Use formal terms such as `marking`, `enabled transition`, `firing`, `pre-set`, and `post-set` when they help, but define them naturally.
- Never claim deadlock freedom, liveness, boundedness, or reachability proofs unless the user supplied a proof artifact or a deterministic analysis tool produced that result.
- If arc weights, inhibitor arcs, reset arcs, capacities, or timing semantics are not specified, assume ordinary unit-weight Petri-net arcs only if that assumption is reasonable, and say so.
- If names are semantically rich, use them to explain the model. If names are abstract like `p1`, `t2`, stay structural unless the user gives domain context.

## References

- Read [references/petri-net-basics.md](references/petri-net-basics.md) when you need a compact terminology refresh.
- Read [references/explanation-template.md](references/explanation-template.md) when the user wants a structured walkthrough or a teaching-oriented answer.
- Read [references/common-structures.md](references/common-structures.md) when identifying common modeling motifs such as choice, synchronization, or resource cycling.

## Example Prompt Shapes

- "Explain what this Petri net is doing."
- "Given this marking, which transitions are enabled?"
- "Walk me through firing `t_start` and then `t_finish`."
- "Interpret this small workflow net in plain English."
- "Tell me whether this model looks like synchronization, mutual exclusion, or a producer-consumer loop."

## Boundaries

This first version is optimized for explanation, not exhaustive verification. If the user asks for formal analysis, route toward a separate analyzer-style skill rather than overclaiming here.
