# Analysis Playbook

Use this playbook for repeatable analyzer behavior.

## Step 1: Classify the Input

Determine whether the user provided:

- a net definition,
- a marking,
- a model fragment,
- Rust code,
- an analysis question,
- or a conceptual workflow.

## Step 2: Pick a Lane

- Pick `PTPN` for ordinary net structure and marking behavior.
- Pick `RustPTA` for code-first concurrency analysis.
- Pick `CVN` for colored or semantically rich token systems.

## Step 3: Normalize

Extract the smallest stable representation possible:

- places,
- transitions,
- arcs,
- weights,
- token classes,
- guards,
- initial marking,
- code entities,
- synchronization primitives.

## Step 4: Analyze Conservatively

Possible outputs:

- enabled transitions,
- immediate firing consequences,
- places that can block progress,
- transitions that are currently starved,
- resource cycles,
- code-to-model hazard candidates,
- semantic gaps that prevent stronger claims.

For ordinary P/T nets in the shared JSON schema, prefer the local scripts before giving a purely verbal answer:

- `scripts/parse_simple_net.py` for a quick summary,
- `scripts/enabled_transitions.py` for enabledness,
- `scripts/fire_transition.py` for one-step firing,
- `scripts/incidence_matrix.py` for structural matrix output.

## Step 5: Report Confidence

Use three levels:

- `High`: deterministic structure or backend-produced result.
- `Medium`: direct observation plus mild interpretation.
- `Low`: incomplete artifact or speculative abstraction.

## Step 6: Recommend Next Action

Examples:

- request the full marking,
- request missing arc weights,
- switch to explainer wording,
- add a backend script wrapper,
- escalate to formal verification.
