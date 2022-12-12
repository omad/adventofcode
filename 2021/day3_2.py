

data = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

from pathlib import Path
import re
import itertools
import numpy as np

data = Path('day5.input').read_text()

def print_diag(diagram):
    for row in diagram.T:
        for val in row:
            if val == 0:
                print(".", end="")
            else:
                print(int(val), end="")
        print()


lines = []
for line in data.splitlines():
    nums = re.findall(r'\d+', line)
    lines.append([int(n) for n in nums])

max_x = max(itertools.chain(*[[x1, x2] for x1, y1, x2, y2 in lines]))
max_y = max(itertools.chain(*[[y1, y2] for x1, y1, x2, y2 in lines]))


diagram = np.zeros([max_x + 1, max_y + 1])

for x1, y1, x2, y2 in lines:
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        diagram[x1, y1:y2+1] += 1
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        diagram[x1:x2+1, y1] += 1

overlaps = (diagram >= 2).sum()

#print_diag(diagram)
print(overlaps)

#diagram = np.zeros([max_x + 1, max_y + 1])
print(lines)
for i, (x1, y1, x2, y2) in enumerate(lines):
    if x1 != x2 and y1 != y2:
#        y1, y2 = min(y1, y2), max(y1, y2)
#        x1, x2 = min(x1, x2), max(x1, x2)
#        print(f"Adding {i} {x1} {y1} {x2} {y2}")

        if x2>x1:
            x2+=1
            xstep = 1
        elif x1>x2:
            x2-=1
            xstep = -1
        if y2>y1:
            y2+=1
            ystep = 1
        elif y1>y2:
            y2-=1
            ystep = -1
        for x, y in zip(range(x1, x2, xstep), range(y1, y2, ystep)):
#            print(x, y)
            diagram[x,y] += 1

#print_diag(diagram)
overlaps = (diagram >= 2).sum()

print(overlaps)
