import sys

if len(sys.argv) != 2:
    print("usage: condition <txt file name>", file=sys.stderr)
    sys.exit(1)

base_file = sys.argv[1].split(".")[0]

with open(sys.argv[1], "r") as fin:
    with open(base_file + ".md", "w") as fout:
        fout.write(f"""---
title: 
from: 
occasion: 
date: 
---
[website](http://javafoundry.com/elc/elc{int(base_file)}.html)

## Synopsis

## Transcript
""")
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
                if width > 200:
                    fout.write("\n")
                    width = 0
                else:
                    if not newline:
                        fout.write(c)
                    newline = False
            else:
                fout.write(c)
                width += 1
