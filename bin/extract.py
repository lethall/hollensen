#!/usr/bin/env python

import json

with open("output.json", "r") as f:
    o = json.load(f)

with open("output.txt", "w") as f:
    f.write(o["text"])
