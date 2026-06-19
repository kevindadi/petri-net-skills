#!/usr/bin/env python3
"""Print enabled transitions for a simple Petri net JSON file."""

from __future__ import annotations

import argparse
import json

from net_utils import enabled_transitions, get_marking, load_net


def main() -> None:
    parser = argparse.ArgumentParser(description="List enabled transitions.")
    parser.add_argument("path", help="Path to the net JSON file.")
    args = parser.parse_args()

    net = load_net(args.path)
    result = {
        "initial_marking": get_marking(net),
        "enabled_transitions": enabled_transitions(net),
    }
    print(json.dumps(result, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
