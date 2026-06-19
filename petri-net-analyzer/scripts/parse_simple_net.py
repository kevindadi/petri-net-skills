#!/usr/bin/env python3
"""Load and summarize a simple Petri net JSON file."""

from __future__ import annotations

import argparse
import json

from net_utils import enabled_transitions, get_marking, load_net, place_ids, transition_ids


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize a simple Petri net JSON file.")
    parser.add_argument("path", help="Path to the net JSON file.")
    args = parser.parse_args()

    net = load_net(args.path)
    summary = {
        "name": net.get("metadata", {}).get("name", "unnamed-net"),
        "place_count": len(place_ids(net)),
        "transition_count": len(transition_ids(net)),
        "arc_count": len(net["arcs"]),
        "initial_marking": get_marking(net),
        "enabled_transitions": enabled_transitions(net),
    }
    print(json.dumps(summary, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
