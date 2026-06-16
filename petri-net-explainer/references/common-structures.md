# Common Structures

Use this file when mapping a net to familiar Petri-net motifs.

## Sequential Flow

A token moves through a chain of places and transitions. Explain this as a step-by-step process.

## Choice or Conflict

Multiple transitions compete for the same token or input condition. Explain this as an either-or branching point.

## Synchronization

A transition requires tokens from multiple places before it can fire. Explain this as a join where multiple prerequisites must be present together.

## Parallel Split

One firing produces tokens into multiple places. Explain this as one event enabling parallel downstream activity.

## Resource Cycle

Tokens in a small set of places represent availability and occupancy of a reusable resource. Explain this as acquire/use/release behavior.

## Producer-Consumer Shape

One part of the net places tokens into a buffer-like place while another part removes them. Explain this as supply and consumption coordinated through shared capacity.

## Waiting or Blocking Signal

A place that can accumulate tokens while downstream transitions remain disabled often suggests waiting, backlog, or a blocked handoff. Present this as a hint, not a formal proof.
