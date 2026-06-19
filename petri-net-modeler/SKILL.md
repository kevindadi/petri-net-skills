---
name: petri-net-modeler
description: Generate Petri net models from process descriptions, requirements, workflow narratives, or code-derived concurrency logic. Use when Codex needs to abstract states, resources, events, and token flow into a Petri net; choose between ordinary P/T nets, Rust-concurrency-derived nets, or value-rich CVN-style models; or produce a model plus assumptions and validation checklist.
---

# Petri Net Modeler

## Overview

Turn a requirement, process, or code fragment into a Petri-net model with explicit assumptions. Favor clear modeling intent over maximal detail.

This skill is the construction companion to the explainer and analyzer skills:

- `petri-net-explainer` explains an existing net.
- `petri-net-analyzer` inspects an existing net or abstraction.
- `petri-net-modeler` builds the net in the first place.

## Modeling Lanes

1. `PTPN`
   - Use for ordinary workflow, resource, synchronization, or state-transition models.
2. `RustPTA`
   - Use when the source is Rust or concurrency logic that should be abstracted into a Petri-net view.
3. `CVN`
   - Use when token identity, type, value, or guard-sensitive behavior matters.

## Core Workflow

1. Classify the input:
   - natural-language requirement,
   - workflow description,
   - Rust code or concurrency sketch,
   - partial net fragment.
2. Select the lane:
   - ordinary P/T net,
   - Rust-derived abstraction,
   - value-rich or colored model.
3. Extract modeling primitives:
   - states, resources, events, waiting points, guards, token classes.
4. Build the net:
   - places,
   - transitions,
   - arcs,
   - initial marking,
   - optional weights or guards.
5. State assumptions and omissions:
   - what was inferred,
   - what was not modeled,
   - what should be checked next.
6. Output a validation checklist:
   - missing places,
   - ambiguous transitions,
   - likely bottlenecks,
   - semantics to confirm with the user.

## Output Shape

Default to this structure:

1. `Chosen Lane`
2. `Modeling Intent`
3. `Places`
4. `Transitions`
5. `Arcs`
6. `Initial Marking`
7. `Assumptions`
8. `Validation Checklist`

## Modeling Rules

- Prefer the smallest model that still captures the requested behavior.
- If names are semantically meaningful, reflect that in the model; otherwise keep the model structural.
- Do not invent guards, arc weights, or token classes unless the input implies them.
- If the source is Rust code, preserve a clear mapping from code concepts to net concepts.
- If the source is naturally value-rich, do not flatten it too early; keep the CVN lane explicit.

## References

- Read [../common/net-schema.md](../common/net-schema.md) for the shared output shape expected by the repository.
- Read [references/backend-map.md](references/backend-map.md) for lane roles.
- Read [references/modeling-playbook.md](references/modeling-playbook.md) for the construction workflow.
- Read [references/ptpn-lane.md](references/ptpn-lane.md) for ordinary workflow-net modeling.
- Read [references/rustpta-lane.md](references/rustpta-lane.md) for Rust concurrency abstraction.
- Read [references/cvn-lane.md](references/cvn-lane.md) for value-rich or colored-net modeling.

## Example Prompt Shapes

- "Turn this workflow into a Petri net."
- "Model this Rust synchronization logic as a Petri net."
- "Create a value-aware net for orders that can be pending, paid, or shipped."
- "Generate the smallest net that captures this producer-consumer flow."
- "Give me a model plus the assumptions I should verify."

## Example Use Cases

- "Model this approval workflow as a Petri net."
- "Turn this Rust worker queue into a Petri-net abstraction."
- "Generate a value-aware model for requests that can be new, retrying, or complete."
- "Produce a minimal net for resource acquire/use/release."
- "Give me the places, transitions, and assumptions for this process."

## Boundaries

This first version defines the modeling contract only. It does not yet generate PNML or invoke backend code, but it is structured so those capabilities can be added later.
