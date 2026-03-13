#!/usr/bin/python3
from paralleladb import ParallelADB

outputs = ParallelADB.run(cmd=None, csv="parallel-ips-koeln.csv")

for o in outputs:
    print(o.serial + ": ")
    for r in o.results:
        print(r.replace("\n", ""))
