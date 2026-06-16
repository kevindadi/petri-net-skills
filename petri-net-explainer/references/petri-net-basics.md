# Petri Net Basics

Use this file when you need compact terminology while explaining a model.

## Core Terms

- `Place`: A state holder or condition container.
- `Transition`: An event or action that may fire.
- `Token`: A marker showing that a place currently holds some resource, condition, or control state.
- `Marking`: The full distribution of tokens across places.
- `Arc`: A directed connection between a place and a transition, or a transition and a place.
- `Pre-set of a transition`: The input places that must supply tokens before the transition fires.
- `Post-set of a transition`: The output places that receive tokens after firing.
- `Enabled transition`: A transition whose input requirements are satisfied by the current marking.
- `Firing`: The state change in which enabled transitions consume tokens from input places and produce tokens in output places.

## Default Assumptions

Unless the user says otherwise, interpret examples as ordinary place/transition nets with:

- directed arcs,
- unit arc weights,
- no inhibitor arcs,
- no reset arcs,
- no timing semantics,
- no colored tokens.

State these assumptions whenever they materially affect the explanation.

## Explanation Heuristics

- When place names look like states such as `idle`, `busy`, or `waiting`, explain tokens as "the system is currently in this state."
- When place names look like resources such as `buffer`, `machine`, or `permit`, explain tokens as available capacity or held resources.
- When transitions look like verbs such as `start`, `finish`, `acquire`, or `release`, explain firing as an event moving the system forward.
