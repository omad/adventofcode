import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = f.readlines()

filesystem = defaultdict(list)
currdir = ()

for line in lines[1:]:
    line = line.strip()
    if line.startswith('$ ls'):
        continue
    elif line.startswith('$ cd'):
        newdir = line.split()[2]
        if newdir == '..':
            currdir = currdir[:-1]
        else:
            currdir = currdir + (newdir,)
    elif line.startswith('dir'):
        continue
    else:
        size, name = line.strip().split()
        filesystem[currdir].append((int(size), name))

dir_sizes = defaultdict(int)

fs2 = {'/'.join(k): v for k, v in filesystem.items()}
print(fs2)

alldirs = set()
for k in fs2.keys():
    alldirs.add(k)
    pieces = k.split('/')
    for p in range(len(pieces)):
        alldirs.add('/'.join(pieces[:p]))

total = 0
usedspace = None

dirsizes = set()

for k in alldirs:
    dirsize = 0
    print(f"Calculating {k}")
    for p in fs2.keys():
        if p.startswith(k):
            print(f"  Including {p}")
            dirsize += sum(size for size, _ in fs2[p])
    print(f"  dirsize: {dirsize}")
    dirsizes.add(dirsize)
    if dirsize <= 100000:
        print("  **INCLUDING**")
        total += dirsize


    if usedspace is None:
        usedspace = dirsize

size = 70000000 
currently_avail = size - usedspace

reqd_space = 30000000

extra_reqd = reqd_space - currently_avail

print(f"require an extra {extra_reqd} bytes")

chosen = 0
for d in sorted(dirsizes, reverse=True):
    if d > extra_reqd:
        chosen = d
    else:
        break


print(total)

print(chosen)
