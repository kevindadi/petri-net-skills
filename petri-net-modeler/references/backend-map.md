# Backend Map

Use this file to keep the modeler aligned with the analyzer/explainer split.

## Role Split

### PTPN

Use for:

- ordinary process and workflow nets,
- state/resource abstraction,
- simple structural models,
- initial marking and firing flow.

### RustPTA

Use for:

- Rust code or concurrency sketches,
- threads, locks, channels, and coordination,
- code-to-net abstraction.

### CVN

Use for:

- value-aware or colored token systems,
- guards or token-class-sensitive transitions,
- models where ordinary P/T flattening would lose meaning.

## Selection Rule

Pick the smallest lane that preserves the user's intent. Escalate to CVN only when token identity or data-dependent behavior matters.
