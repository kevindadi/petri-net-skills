#!/usr/bin/env python3
"""Compute the incidence matrix for a simple Petri net JSON file."""

from __future__ import annotations

import argparse
import json

from net_utils import incidence_matrix, load_net


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute the incidence matrix.")
    parser.add_argument("path", help="Path to the net JSON file.")
    args = parser.parse_args()

    net = load_net(args.path)
    places, transitions, matrix = incidence_matrix(net)
    result = {
        "places": places,
        "transitions": transitions,
        "matrix": matrix,
    }
    print(json.dumps(result, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
