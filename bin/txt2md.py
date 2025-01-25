#!/usr/bin/env python
import sys
import pathlib
from collections import defaultdict

MAX_LENGTH = 200
ARCHIVE = "/Users/leehall/hollensen-realmedia"

if len(sys.argv) != 2:
    print("usage: txt2md <txt file name>", file=sys.stderr)
    sys.exit(1)

stem = pathlib.Path(sys.argv[1]).stem

meta = defaultdict(lambda : "")
try:
    with open(f"{ARCHIVE}/meta/{stem}", "r") as m:
        key = None
        for line in m:
            parts = line.split("=")
            if len(parts) >= 2:
                key = parts[0].strip()
                meta[key] = "=".join(parts[1:]).strip()
            elif key:
                value = " ".join(parts).strip()
                meta[key] = f"{meta[key]} {value}"
except:
    print(f"Failed meta for {stem}", file=sys.stderr)

try:
    dp = meta['submitter'].split("/")
    meta['date'] = f"{dp[2]}{int(dp[0]):02d}{int(dp[1]):02d}"
except:
    print(f"Failed meta['date'] for {stem}", file=sys.stderr)

try:
    frontmatter = f"""---
title: {meta['title']}
from: 
occasion: 
date: {meta['date']}
---
[website](http://javafoundry.com/elc/elc{int(stem)}.html)

## Synopsis
{meta['description']}

## Transcript
"""
except:
    frontmatter = 'No Frontmatter\n'

with open(sys.argv[1], "r") as fin:
    with open(stem + ".md", "w") as fout:
        fout.write(frontmatter)
        newline = False
        width = 0
        while True:
            c = fin.read(1)
            if not c:
                break
            elif c in ['?', '.', '!']:
                fout.write(c + "\n\n")
                newline = True
                width = 0
            elif c == '\n':
                if newline:
                    # swallow existing newlines
                    newline = False
                else:
                    fout.write(" ")
            elif c == " ":
                if width > MAX_LENGTH:
                    fout.write("\n")
                    width = 0
                else:
                    if not newline:
                        fout.write(c)
                    newline = False
            else:
                fout.write(c)
                width += 1