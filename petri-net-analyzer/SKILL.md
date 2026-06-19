---
name: petri-net-analyzer
description: Analyze Petri nets, workflow nets, and related concurrency models from text, structured net definitions, markings, or code-derived abstractions. Use when Codex needs to inspect enabled transitions, firing consequences, deadlock risks, boundedness or liveness signals, net structure, or the concurrency behavior of Rust-like systems. This skill is designed as a multi-backend analyzer skeleton that can incorporate PTPN, RustPTA, and CVN style resources.
---

# Petri Net Analyzer

## Overview

Analyze a Petri-net-like model with a bias toward explicit evidence, small-step reasoning, and backend-aware routing. Treat this skill as a coordinator that can combine multiple analysis styles instead of one monolithic method.

This skeleton is designed to fuse three external lines of work:

- `PTPN`: baseline Petri-net / place-transition modeling and analysis support.
- `RustPTA`: Rust-oriented concurrency extraction or analysis flow.
- `CVN`: richer colored or value-aware net semantics beyond a plain P/T model.

Do not imply that all three backends are locally installed or available unless the current workspace actually contains them. If they are absent, use the routing model and output shape below as the integration contract.

## Backend Routing

Choose the primary backend flavor based on the task:

1. Use the `PTPN` lane for:
   - ordinary place/transition nets,
   - structured arc lists,
   - incidence-style reasoning,
   - enabled-transition analysis,
   - basic structural checks.
2. Use the `RustPTA` lane for:
   - Rust concurrency or systems code,
   - lock/channel/thread coordination questions,
   - mapping execution states into net-like abstractions,
   - bridging code behavior to Petri-net reasoning.
3. Use the `CVN` lane for:
   - colored tokens,
   - value-carrying or typed token semantics,
   - typed token semantics,
   - richer guard or value-flow interpretation,
   - requests that need a more expressive model than a plain P/T net.
4. Combine lanes only when the handoff is explicit:
   - for example, derive a concurrency abstraction from RustPTA-style reasoning, then interpret the resulting net with PTPN-style structure, then enrich the report with CVN-style token semantics if needed.

## Core Workflow

1. Identify the artifact type:
   - text net definition,
   - Petri-net file,
   - code excerpt,
   - conceptual process description,
   - existing analysis result.
2. Pick the primary backend lane and say why.
3. Normalize the model:
   - places, transitions, arcs, weights, token kinds, marking, code entities, or control states.
4. Perform analysis at the strongest justified level:
   - enabled transitions,
   - firing consequences,
   - local deadlock candidates,
   - structural bottlenecks,
   - boundedness hints,
   - liveness hints,
   - code-to-net mapping observations.
5. Separate facts from heuristics:
   - backend-computed result,
   - directly observed structure,
   - plausible but unproven inference.
6. Recommend the next deeper action:
   - run a backend script,
   - provide a fuller model,
   - switch to explainer mode,
   - switch to a future formal verifier.

## Output Shape

Default to this output structure:

1. `Artifact Type`
2. `Chosen Analysis Lane`
3. `Normalized Model`
4. `Immediate Findings`
5. `Risk Signals or Open Questions`
6. `Confidence Level`
7. `Suggested Next Step`

When using more than one lane, add a short `Lane Handoff` section that explains what each lane contributed.

## Analysis Rules

- Never present a liveness, reachability, boundedness, or deadlock-freedom claim as proven unless it came from a deterministic backend computation or a user-supplied proof artifact.
- For code-derived reasoning, be explicit about abstraction loss: a Rust code path mapped into a Petri net is an analysis model, not the program itself.
- If colored tokens, guards, or higher-level semantics are present, avoid flattening them into a plain P/T net without saying what meaning is lost.
- If a value-rich or colored-net backend is more appropriate than a plain P/T analysis, say so explicitly and route into the CVN lane.
- If the user asks for an explanation rather than a diagnosis, prefer the explainer skill or a lighter analyzer response.

## Planned Integration Surface

Use these files as the integration contract for future implementation:

- [../common/net-schema.md](../common/net-schema.md): shared repository-wide intermediate representation.
- [references/backend-map.md](references/backend-map.md): role split among PTPN, RustPTA, and CVN.
- [references/analysis-playbook.md](references/analysis-playbook.md): repeatable analysis procedure.
- [references/ptpn-lane.md](references/ptpn-lane.md): baseline P/T-net lane behavior and expectations.
- [references/rustpta-lane.md](references/rustpta-lane.md): Rust concurrency abstraction lane.
- [references/cvn-lane.md](references/cvn-lane.md): value-rich or colored-net lane.
- [references/integration-roadmap.md](references/integration-roadmap.md): how to evolve this skeleton into a real composite toolchain.

## Available Scripts

For ordinary P/T nets using the shared JSON shape:

- `scripts/parse_simple_net.py`
- `scripts/enabled_transitions.py`
- `scripts/fire_transition.py`
- `scripts/incidence_matrix.py`

Use these scripts for deterministic first-pass analysis before escalating to richer backends.

## Example Prompt Shapes

- "Analyze this Petri net for enabled transitions and deadlock risk."
- "Map this Rust synchronization logic into a Petri-net-style model and explain the hazards."
- "Use a P/T-net view first, then tell me where colored-token semantics would matter."
- "Given this marking and arc list, summarize the immediate reachable behaviors."
- "Help me design a unified analyzer workflow that can later call PTPN, RustPTA, and CVN."

## Example Use Cases

- "Check whether this model has a deadlock candidate."
- "What transitions are enabled in this marking, and why?"
- "Analyze this Rust channel/lock pattern as a Petri-net abstraction."
- "Estimate whether this net looks bounded or resource-limited."
- "Tell me whether a CVN-style lane is needed for this model."

## Boundaries

This version is a repository skeleton, not a finished backend bundle. It should stay honest about which capabilities are implemented locally and which are planned integration points.
