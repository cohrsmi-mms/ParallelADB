#!/usr/bin/python3
import sys
from paralleladb import ParallelADB

if len(sys.argv) > 1:
    csvFile = sys.argv[1]
else:
    print("Usage: " + sys.argv[0] + " [text file containing newline-separated ip addresses]")
    exit(1)

outputs = ParallelADB.run(cmd=None, csv=csvFile)

for o in outputs:
    print(o.serial + ": ")
    for r in o.results:
        print(r.replace("\n", ""))
