import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

elves = []

cur = 0
for line in lines:
    if line == '\n':
        elves.append(cur)
        cur = 0
    else:
        num = int(line.strip())
        cur += num

print(max(elves))

print(list(sorted(elves)))
print(sum(list(sorted(elves, reverse=True))[0:3]))
