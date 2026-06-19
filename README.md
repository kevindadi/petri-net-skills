# Petri Net Skills

This repository contains a three-skill Petri-net toolkit.

## Skills

- [petri-net-explainer](./petri-net-explainer/SKILL.md): explain an existing Petri net in plain language.
- [petri-net-analyzer](./petri-net-analyzer/SKILL.md): inspect an existing net or code-derived abstraction.
- [petri-net-modeler](./petri-net-modeler/SKILL.md): build a Petri net from a requirement, workflow, or code sketch.

## Shared Assets

- [common/net-schema.md](./common/net-schema.md): shared intermediate representation for structured nets.
- [examples/producer-consumer/README.md](./examples/producer-consumer/README.md): first cross-skill example artifact.

## Recommended Flow

1. Use `petri-net-modeler` to turn an idea into a net.
2. Use `petri-net-analyzer` to check the net for structural or behavioral issues.
3. Use `petri-net-explainer` to present the net clearly to a human.

## Backend Lanes

The analyzer and modeler both route through these lanes:

- `PTPN` for ordinary place/transition nets.
- `RustPTA` for Rust concurrency abstractions.
- `CVN` for value-aware or colored-token models.

Choose the smallest lane that preserves the user's intent.
