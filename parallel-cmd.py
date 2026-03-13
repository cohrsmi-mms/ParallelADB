#!/usr/bin/python3
from paralleladb import ParallelADB

DATE="2026-03-13"
outputs = ParallelADB.run('su 0 "grep \\"error: 4\\" /data/user/0/de.xplace.android.beeceen.app/files/xplace/logs/' + DATE + '.log"')
#outputs = ParallelADB.run('su 0 "grep \\"Ad complete\\" /data/user/0/de.xplace.android.beeceen.app/files/xplace/logs/' + DATE + '.log"')
#outputs = ParallelADB.run('su 0 "grep \\"ignoring\\" /data/user/0/de.xplace.android.beeceen.app/files/xplace/logs/' + DATE + '.log"')
#outputs = ParallelADB.run('date')

for o in outputs:
    print(o.serial + ": ")
    for r in o.results:
        #print (r.replace("\\n", "\n"))
        print(r.replace("\n", ""))
