#!/usr/bin/python3
import sys
from paralleladb import ParallelADB

root = False
if len(sys.argv) > 1:
    csvFile = sys.argv[1]
else:
    print("Usage: " + sys.argv[0] + " {text file containing newline-separated ip addresses} [root]")
    exit(1)
if len(sys.argv) > 2 and sys.argv[2] == "root":
    root = True

outputs = ParallelADB.run(cmd=None, csv=csvFile)
for o in outputs:
    print(o.serial + ": ")
    for r in o.results:
        print(r.replace("\n", ""))

if root:
    outputs = ParallelADB.run("root", is_shell_cmd=False)
    for o in outputs:
        print(o.serial + ": ")
        for r in o.results:
            print(r.replace("\n", ""))
