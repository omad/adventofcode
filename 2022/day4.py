
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

def range_to_set(r):
    s, e = [int(n) for n in r.split('-')]
    return set(range(s, e+1))
    

complete_overlaps = 0
overlaps = 0
for line in lines:
    first, second = line.strip().split(',')

    first = range_to_set(first)
    second = range_to_set(second)

    if first.issubset(second) or second.issubset(first):
        complete_overlaps += 1

    if not first.isdisjoint(second):
        overlaps += 1

print(complete_overlaps)
print(overlaps)
    

