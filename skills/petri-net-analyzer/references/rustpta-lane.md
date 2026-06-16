# RustPTA Lane

Use this lane when the task starts from Rust or Rust-like concurrency logic.

## Scope

- inspect code-level coordination patterns,
- identify concurrency entities,
- propose a Petri-net abstraction of threads, resources, channels, or locks,
- connect code behavior to net-style hazard reasoning.

## Abstraction Targets

- threads or tasks,
- mutex or semaphore ownership,
- send/receive channels,
- wait/notify points,
- resource acquisition and release cycles.

## Good Outputs

- a code-to-net mapping table,
- likely blocking or waiting states,
- resource contention notes,
- suggested Petri-net fragments for further analysis.

## Cautions

- preserve the distinction between program semantics and abstraction semantics,
- mention when a mapping ignores timing, fairness, or data-dependent control flow,
- avoid claiming that the abstraction is complete unless it clearly is.
