# Modeling Playbook

Use this playbook to turn an input into a net model.

## Step 1: Understand the Source

Identify whether the user supplied:

- a process description,
- a requirement,
- a workflow,
- Rust code,
- a partial net.

## Step 2: Decide the Semantic Level

- Use `PTPN` for structural flows.
- Use `RustPTA` for concurrency abstractions.
- Use `CVN` for token-value or guard-sensitive behavior.

## Step 3: Extract Modeling Primitives

- states,
- resources,
- events,
- synchronization points,
- waiting conditions,
- token classes,
- guards.

## Step 4: Draft the Net

Produce:

- places,
- transitions,
- arcs,
- initial marking,
- optional weights or guards.

## Step 5: Add Modeling Notes

Explain:

- why the chosen lane fits,
- what was abstracted away,
- what should be validated next.

## Step 6: Produce a Checklist

Include items such as:

- ambiguous states,
- omitted branches,
- missing resources,
- potential over- or under-modeling,
- semantic assumptions to confirm.
