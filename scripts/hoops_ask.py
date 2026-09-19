#!/usr/bin/env python3
"""Thin wrapper so `python scripts/hoops_ask.py` works from the repo root."""

from hoops_data.ask import main

if __name__ == "__main__":
    raise SystemExit(main())
