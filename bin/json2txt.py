#!/usr/bin/env python
import sys
import json
with open("output.json", "r") as f:
    segments = json.load(f)['segments']

with open(sys.argv[1], "w") as fo:
    for s in segments:
        print(s['text'].strip(), file=fo)
