# Net Schema

Use this schema as the repository-wide intermediate representation for ordinary P/T nets and nearby extensions.

## Design Goals

- make `petri-net-modeler` outputs consumable by `petri-net-analyzer`,
- make `petri-net-explainer` explanations reference the same object model,
- leave room for future `CVN` and `RustPTA`-derived metadata without breaking simple workflows.

## Canonical Shape

```json
{
  "metadata": {
    "name": "producer-consumer",
    "lane": "PTPN",
    "source_type": "workflow-description"
  },
  "places": [
    { "id": "p_idle", "label": "Idle producer" },
    { "id": "p_buffer", "label": "Buffer", "capacity": 1 }
  ],
  "transitions": [
    { "id": "t_produce", "label": "Produce item" },
    { "id": "t_consume", "label": "Consume item" }
  ],
  "arcs": [
    { "source": "p_idle", "target": "t_produce", "weight": 1 },
    { "source": "t_produce", "target": "p_buffer", "weight": 1 }
  ],
  "initial_marking": {
    "p_idle": 1,
    "p_buffer": 0
  },
  "token_types": [],
  "guards": [],
  "extensions": {}
}
```

## Required Fields

- `places`
- `transitions`
- `arcs`
- `initial_marking`

## Field Notes

### `metadata`

Optional metadata about origin and modeling lane.

Suggested keys:

- `name`
- `lane`
- `source_type`
- `notes`

### `places`

Array of objects with:

- `id` required
- `label` optional
- `capacity` optional
- `kind` optional

### `transitions`

Array of objects with:

- `id` required
- `label` optional
- `kind` optional

### `arcs`

Array of objects with:

- `source` required
- `target` required
- `weight` optional, default `1`
- `kind` optional for future extensions

For the first script generation, assume ordinary arcs only. `source` and `target` must connect a place to a transition or a transition to a place.

### `initial_marking`

Object keyed by place id with integer token counts.

Missing place ids default to `0` in current analyzer scripts, but modelers should emit every place explicitly when possible.

### `token_types`

Reserved for `CVN` or other richer semantics. Keep it as an empty array for ordinary P/T nets.

### `guards`

Reserved for value-aware or guarded transitions. Keep it as an empty array for ordinary P/T nets.

### `extensions`

Reserved for backend-specific payloads such as Rust abstraction notes or richer token semantics.

## Validation Expectations

For the first analyzer scripts:

- place ids must be unique,
- transition ids must be unique,
- arc endpoints must exist,
- weights must be positive integers,
- initial marking values must be non-negative integers.

## First-Phase Constraints

The initial scripts in `petri-net-analyzer/scripts/` support:

- ordinary place/transition nets,
- ordinary weighted arcs,
- single-step firing,
- incidence matrix generation.

They do not yet support:

- inhibitor arcs,
- reset arcs,
- timed semantics,
- colored-token evaluation,
- guard evaluation.
