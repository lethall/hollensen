#!/usr/bin/env python
import sys
import json
with open("output.json", "r") as f:
    segments = json.load(f)['segments']

with open(sys.argv[1], "w") as fo:
    last_minute = None
    for s in segments:
        minute = f"{s['end']//60:.0f}"
        text = s['text'].strip()
        print(text, file=fo)
        if minute != last_minute and text.endswith(".") and minute != "0":
            print(f"##### {f"{s['end']//60:02.0f}:{s['end']%60:02.0f}"}", file=fo)
            last_minute = minute
