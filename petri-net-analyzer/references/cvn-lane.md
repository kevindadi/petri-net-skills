# CVN Lane

Use this lane when colored tokens, value-carrying tokens, or richer semantic distinctions matter.

## Scope

- explain typed or value-aware tokens,
- preserve distinctions between token classes or token values,
- account for guards or value-dependent enabling behavior,
- highlight where a plain P/T reduction would lose important information.

## Typical Triggers

- references to colored Petri nets or richer net variants,
- tokens that represent different jobs, users, packets, requests, or values,
- guards or transition logic that depends on token content,
- questions focused on modeling expressiveness beyond ordinary place/transition nets.

## Good Outputs

- a clear explanation of token domains or token classes,
- an explicit note about which transitions depend on token values or guards,
- a contrast between the richer model and a flattened P/T approximation,
- a recommendation about whether to stay value-aware during further analysis.

## Cautions

- do not flatten away value-dependent behavior unless the user asks for an approximation,
- preserve guard semantics when they influence enabledness,
- be explicit when a backend or artifact is only partially expressive for the model at hand.
