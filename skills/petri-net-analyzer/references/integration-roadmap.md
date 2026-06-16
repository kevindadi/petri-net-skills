# Integration Roadmap

Use this file when turning the analyzer skeleton into a working multi-backend skill.

## Phase 1: Skill-Level Fusion

Goal:

- unify prompts,
- unify output shape,
- unify backend routing language.

Deliverables:

- `SKILL.md`,
- backend lane references,
- example prompts,
- consistent confidence reporting.

## Phase 2: Local Wrappers

Add `scripts/` wrappers once the upstream projects are available locally.

Suggested wrappers:

- `scripts/run_ptpn_analysis.*`
- `scripts/run_rustpta_analysis.*`
- `scripts/run_cpn_guidance.*`
- `scripts/unified_analyze.*`

Each wrapper should:

- accept a normalized input format,
- capture stdout and stderr cleanly,
- return machine-readable summaries when possible,
- preserve provenance of which backend produced which result.

## Phase 3: Shared Intermediate Representation

Define a repository-local intermediate representation so all lanes can exchange data:

- places,
- transitions,
- arcs,
- weights,
- token classes,
- guards,
- marking,
- source provenance,
- abstraction notes.

## Phase 4: Composite Workflows

Examples:

1. Parse code with the RustPTA lane.
2. Emit a net-like IR.
3. Run PTPN-style structural analysis.
4. If token classes or value semantics matter, enrich the report with CVN-style interpretation.

## Phase 5: Validation

Validate the integrated analyzer on:

- a toy mutex example,
- a producer-consumer example,
- a workflow net,
- a colored-token routing example.

Keep validation artifacts close to the repository once the implementation exists.
