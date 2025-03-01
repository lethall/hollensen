#!/usr/bin/env python
import sys
from collections import defaultdict
import pathlib
from sqlite3 import connect

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
    dt = "/".join((date[4:6], date[6:], date[:4]))
    meta["date"] = dt

with connect("sermon_meta.db") as db:
    db.execute("create table if not exists meta (id primary key, title, reading, occasion, preached, dateseq)")
    db.execute("begin")
    db.execute("delete from meta where id = ?", (meta["sermon_id"],))
    db.execute("insert into meta (id,title,reading,occasion,preached,dateseq) values (?,?,?,?,?,?)",
               (meta["sermon_id"], meta["title"], meta["from"], meta["occasion"], meta["date"], date))
    db.commit()
