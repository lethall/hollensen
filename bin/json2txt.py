#!/usr/bin/env python
import sys
import json

REPLACEMENTS = (
    ("until life", "unto life"),
    ("word of God", "Word of God"),
    ("Emmanuel", "Emanuel")
)
with open("output.json", "r") as f:
    segments = json.load(f)['segments']

with open(sys.argv[1], "w") as fo:
    last_minute = None
    for s in segments:
        timestamp = s['end']
        minute = timestamp//60
        text = s['text'].strip()
        for from_txt, to_txt in REPLACEMENTS:
            text = text.replace(from_txt, to_txt)
        if not text[-1] in ".?!":
            print(text, file=fo, end=" ")
            continue
        print(text + "\n", file=fo)
        if minute != last_minute  and minute:
            print(f"##### {timestamp//60:02.0f}:{timestamp%60:02.0f}\n", file=fo)
            last_minute = minute
