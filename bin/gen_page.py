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

in_synopsis = False
synopsis = []
start_transcript = 0
for ln in md_data:
  start_transcript += 1
  ln = ln.strip()
  if in_synopsis:
    if ln == "## Transcript":
      break
    synopsis.append(ln)
    continue
  if ln == "## Synopsis":
    in_synopsis = True

meta["synopsis"] = "</h3>\n<h3>".join(synopsis)

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
      <tr><td><img src=left_image.gif></td>
        <td align="center"><h1>"${title}"</h1><h1>${from}</h1></td>
        <td><img src=right_image.gif></td></tr>
      <tr><td></td><td align="center">This sermon was preached ${date} at Emanuel Lutheran Church in Marion, OH</td><td></td></tr>
      <tr><td></td><td align="center"><h2>${occasion}</h2></td><td></td></tr>
    </table>
    <h3>${synopsis}</h3>
    <br>
  </center>
  <audio id="audioPlayer" class="floating-audio" controls>
    <source src="/hollensen/${sermon_id}.mp3" type="audio/mpeg">
  </audio>
  <article id="transcript" class="markdown-body">
  ${body}
  </article>
  <script src="hollensen.js"></script>
</body>

</html>'''

page = TEMPLATE
for k in meta.keys():
    page = page.replace("${" + k + "}", meta[k])

with open(meta["sermon_id"] + ".html", "w") as f:
    f.write(page.replace("${body}", markdown("".join(md_data[start_transcript:]))))
