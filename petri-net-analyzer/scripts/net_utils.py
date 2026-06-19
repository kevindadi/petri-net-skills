#!/usr/bin/env python3
"""Shared helpers for simple P/T-net analyzer scripts."""

from __future__ import annotations

import json
from pathlib import Path


def load_net(path_str: str) -> dict:
    path = Path(path_str)
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    validate_net(data)
    return data


def validate_net(net: dict) -> None:
    if not isinstance(net, dict):
        raise ValueError("Net must be a JSON object.")

    for key in ("places", "transitions", "arcs", "initial_marking"):
        if key not in net:
            raise ValueError(f"Missing required field: {key}")

    places = net["places"]
    transitions = net["transitions"]
    arcs = net["arcs"]
    marking = net["initial_marking"]

    place_ids = [place["id"] for place in places]
    transition_ids = [transition["id"] for transition in transitions]

    if len(place_ids) != len(set(place_ids)):
        raise ValueError("Place ids must be unique.")
    if len(transition_ids) != len(set(transition_ids)):
        raise ValueError("Transition ids must be unique.")

    place_set = set(place_ids)
    transition_set = set(transition_ids)
    node_set = place_set | transition_set

    for arc in arcs:
        source = arc["source"]
        target = arc["target"]
        weight = arc.get("weight", 1)

        if source not in node_set:
            raise ValueError(f"Unknown arc source: {source}")
        if target not in node_set:
            raise ValueError(f"Unknown arc target: {target}")
        if (source in place_set and target in place_set) or (
            source in transition_set and target in transition_set
        ):
            raise ValueError(
                f"Arc {source} -> {target} must connect a place and a transition."
            )
        if not isinstance(weight, int) or weight <= 0:
            raise ValueError(
                f"Arc {source} -> {target} must have a positive integer weight."
            )

    for place_id, tokens in marking.items():
        if place_id not in place_set:
            raise ValueError(f"Initial marking references unknown place: {place_id}")
        if not isinstance(tokens, int) or tokens < 0:
            raise ValueError(
                f"Initial marking for {place_id} must be a non-negative integer."
            )


def place_ids(net: dict) -> list[str]:
    return [place["id"] for place in net["places"]]


def transition_ids(net: dict) -> list[str]:
    return [transition["id"] for transition in net["transitions"]]


def get_marking(net: dict) -> dict[str, int]:
    ordered = {place_id: 0 for place_id in place_ids(net)}
    ordered.update(net["initial_marking"])
    return ordered


def input_arcs(net: dict, transition_id: str) -> list[dict]:
    transitions = set(transition_ids(net))
    if transition_id not in transitions:
        raise ValueError(f"Unknown transition: {transition_id}")
    return [
        arc
        for arc in net["arcs"]
        if arc["target"] == transition_id and arc["source"] not in transitions
    ]


def output_arcs(net: dict, transition_id: str) -> list[dict]:
    transitions = set(transition_ids(net))
    if transition_id not in transitions:
        raise ValueError(f"Unknown transition: {transition_id}")
    return [
        arc
        for arc in net["arcs"]
        if arc["source"] == transition_id and arc["target"] not in transitions
    ]


def is_enabled(net: dict, transition_id: str, marking: dict[str, int] | None = None) -> bool:
    current = get_marking(net) if marking is None else dict(marking)
    for arc in input_arcs(net, transition_id):
        if current.get(arc["source"], 0) < arc.get("weight", 1):
            return False
    return True


def enabled_transitions(net: dict, marking: dict[str, int] | None = None) -> list[str]:
    current = get_marking(net) if marking is None else dict(marking)
    return [
        transition_id
        for transition_id in transition_ids(net)
        if is_enabled(net, transition_id, current)
    ]


def fire_transition(net: dict, transition_id: str, marking: dict[str, int] | None = None) -> dict[str, int]:
    current = get_marking(net) if marking is None else dict(marking)
    if not is_enabled(net, transition_id, current):
        raise ValueError(f"Transition {transition_id} is not enabled.")

    next_marking = dict(current)
    for arc in input_arcs(net, transition_id):
        next_marking[arc["source"]] -= arc.get("weight", 1)
    for arc in output_arcs(net, transition_id):
        next_marking[arc["target"]] = next_marking.get(arc["target"], 0) + arc.get("weight", 1)
    return next_marking


def incidence_matrix(net: dict) -> tuple[list[str], list[str], list[list[int]]]:
    places = place_ids(net)
    transitions = transition_ids(net)
    pre = {(place, transition): 0 for place in places for transition in transitions}
    post = {(place, transition): 0 for place in places for transition in transitions}

    transition_set = set(transitions)
    for arc in net["arcs"]:
        weight = arc.get("weight", 1)
        if arc["target"] in transition_set:
            pre[(arc["source"], arc["target"])] += weight
        elif arc["source"] in transition_set:
            post[(arc["target"], arc["source"])] += weight

    rows = []
    for place in places:
        row = []
        for transition in transitions:
            row.append(post[(place, transition)] - pre[(place, transition)])
        rows.append(row)
    return places, transitions, rows
