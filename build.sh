#!/bin/sh
# Build the static site from the Markdown docs.
# Works with any Python 3.4+; no external packages needed.
python3 build/build.py "$@"
