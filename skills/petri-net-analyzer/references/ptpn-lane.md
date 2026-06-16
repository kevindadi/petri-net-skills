# PTPN Lane

Use this lane for ordinary place/transition net analysis.

## Scope

- parse a small net description,
- identify pre-sets and post-sets,
- determine enabled transitions from a marking,
- explain one-step or short-horizon firing results,
- surface structural hotspots.

## Expected Inputs

- text definitions of places, transitions, arcs, and marking,
- simple PN-like structured data,
- analysis questions framed around ordinary P/T nets.

## Good Outputs

- normalized place/transition tables,
- enabled-transition list,
- stepwise firing explanation,
- local deadlock candidate notes,
- simple structure summary.

## Cautions

- do not overclaim formal properties without computation,
- do not silently erase weighted arcs if they matter,
- do not collapse colored semantics into this lane without warning.
