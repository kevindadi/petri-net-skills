#!/usr/bin/env python3
"""Fire a single transition for a simple Petri net JSON file."""

from __future__ import annotations

import argparse
import json

from net_utils import fire_transition, get_marking, load_net


def main() -> None:
    parser = argparse.ArgumentParser(description="Fire a transition once.")
    parser.add_argument("path", help="Path to the net JSON file.")
    parser.add_argument("transition", help="Transition id to fire.")
    args = parser.parse_args()

    net = load_net(args.path)
    before = get_marking(net)
    after = fire_transition(net, args.transition, before)
    result = {
        "transition": args.transition,
        "before": before,
        "after": after,
    }
    print(json.dumps(result, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
