# Producer Consumer Example

This example is the first shared test artifact for the three Petri-net skills.

## Files

- `net.json`: repository-standard ordinary P/T-net representation.

## Intended Use

- `petri-net-modeler`: use this as a target shape for generated structured output.
- `petri-net-analyzer`: use this as a script input for enabled-transition, firing, and incidence checks.
- `petri-net-explainer`: use this as a teaching-oriented walkthrough example.

## Expected Behavior

- Initial enabled transition: `t_produce`
- Initially disabled transition: `t_consume`
- After firing `t_produce`, `t_consume` becomes enabled

## Good Prompt Examples

- "Explain this producer-consumer Petri net."
- "Analyze enabled transitions for this net."
- "Generate a Petri net like this from a producer-consumer description."
