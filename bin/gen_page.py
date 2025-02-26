#!/usr/bin/env python
import sys
from collections import defaultdict
import pathlib

from markdown import markdown

meta = defaultdict(lambda : "")
meta["sermon_id"] = pathlib.Path(sys.argv[1]).stem

with open(sys.argv[1], "r") as f:
    md_data = f.readlines()

for ln in md_data:
    if ln.startswith("#"):
        break
    for key in ("title: ", "from: ", "occasion: ", "date: "):
        if ln.startswith(key):
            meta[key[:-2]] = ln[len(key) : ].strip()
            break
        continue

date = meta["date"]
if date:
    date = "/".join((date[4:6], date[6:], date[:4]))
    meta["date"] = date

TEMPLATE = '''
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">

  <title>${title}</title>
  <link rel="stylesheet" href="github-markdown.css">
  <link rel="stylesheet" href="hollensen.css">
</head>

<body>
  <center class="heading">

    <table>
      <tr><td><img src=pulpit_sm.gif></td><td><h1>"${title}"</h1></td><td><img src=portrait_sm.gif></td></tr>
      <tr><td></td><td align="center">This sermon was preached ${date} at Emanuel Lutheran Church in Marion, OH</td><td></td></tr>
      <tr><td></td><td align="center"><h2>${occasion}</h2></td><td></td></tr>
    </table>
  </center>
  <audio class="floating-audio" controls src="/hollensen/${sermon_id}.mp3">
    <a href="/hollensen/${sermon_id}.mp3">Download audio</a>
  </audio>
  <article class="markdown-body">
  ${body}
  </article>
</body>

</html>'''

page = TEMPLATE
for k in meta.keys():
    page = page.replace("${" + k + "}", meta[k])

with open(meta["sermon_id"] + ".html", "w") as f:
    f.write(page.replace("${body}", markdown("".join(md_data))))
