# Backend Map

Use this file to keep the three-library fusion coherent.

## Intent

The analyzer should not treat all Petri-net-related tasks as the same problem. Split them into lanes so each external project contributes a clear role.

## Proposed Role Split

### PTPN

Primary lane for:

- plain place/transition net representation,
- arc and marking normalization,
- incidence-style structure,
- enabled-transition checks,
- firing-step evolution,
- small structural summaries.

### RustPTA

Primary lane for:

- Rust code analysis,
- thread, channel, lock, and resource coordination patterns,
- code-to-net abstraction,
- concurrency risk surfacing before or alongside Petri-net formalization.

### CVN

Primary lane for:

- colored-token semantics,
- value-carrying tokens,
- guarded or richer token transformations,
- typed or value-carrying token explanation,
- interpretation support when a plain P/T view is too lossy.

## Analyzer Modes

1. `pt-net`
2. `rust-concurrency`
3. `cpn`
4. `hybrid`

Hybrid mode should name the lead lane and any secondary lane. Avoid mixing all three unless the user clearly benefits from it.
