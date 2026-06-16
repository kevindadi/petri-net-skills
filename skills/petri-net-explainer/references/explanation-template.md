# Explanation Template

Use this template when the user wants a clean walkthrough.

## Overview

Summarize what the net appears to model in one or two sentences.

## Elements

- Explain each place in operational terms.
- Explain each transition as an event or state change.
- Mention any arc that creates an important dependency.

## Current Marking

- Describe where the tokens are.
- Translate that token distribution into a state-of-the-system interpretation.

## Enabled Transitions

For each candidate transition:

- name the required input places,
- say whether the current marking satisfies them,
- explain the result in plain language.

## Possible Next Step

Walk through one firing:

1. name consumed tokens,
2. name produced tokens,
3. describe the resulting state.

## Behavioral Notes

Call out any visible pattern:

- sequential flow,
- branching choice,
- synchronization,
- mutual exclusion,
- repeated cycle,
- waiting or blocking state.

## Assumptions

List any missing information that limits certainty.
