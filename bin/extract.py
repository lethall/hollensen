#!/usr/bin/env python
import sys
import json

if len(sys.argv) != 2:
    print("usage: extract <txt file name>", file=sys.stderr)
    sys.exit(1)

with open("output.json", "r") as f:
    o = json.load(f)

with open(f"src/{sys.argv[1]}.txt", "w") as f:
    f.write(o["text"])
