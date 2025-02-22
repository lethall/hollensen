#!/usr/bin/env python
import sys
import json
with open("output.json", "r") as f:
    segments = json.load(f)['segments']

with open(sys.argv[1], "w") as fo:
    last_minute = None
    for s in segments:
        timestamp = s['end']
        minute = timestamp//60
        text = s['text'].strip()
        print(text, file=fo)
        if minute != last_minute and text[-1] in ".?!" and minute:
            print(f"##### {timestamp//60:02.0f}:{timestamp%60:02.0f}", file=fo)
            last_minute = minute
