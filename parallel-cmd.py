#!/usr/bin/python3
from paralleladb import ParallelADB

#DATE="2026-04-02"
#outputs = ParallelADB.run('su 0 "grep \\"error: 4\\" /data/user/0/de.xplace.android.beeceen.app/files/xplace/logs/' + DATE + '.log"')
#outputs = ParallelADB.run('su 0 "grep \\"Ad complete\\" /data/user/0/de.xplace.android.beeceen.app/files/xplace/logs/' + DATE + '.log"')
#outputs = ParallelADB.run('su 0 "grep \\"ignoring\\" /data/user/0/de.xplace.android.beeceen.app/files/xplace/logs/' + DATE + '.log"')
#outputs = ParallelADB.run('date')
outputs = ParallelADB.run('su 0 "du -sch /data/user/0/com.android.providers.downloads/cache"')
#outputs = ParallelADB.run('ls -l /data/user/0/com.android.providers.downloads/cache | head')
#outputs = ParallelADB.run('rm -rvf /data/user/0/com.android.providers.downloads/cache/*')

for o in outputs:
    print(o.serial + ": ")
    for r in o.results:
        print(r.replace("\n", ""))
