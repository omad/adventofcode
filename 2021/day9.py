

data = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""

from collections import defaultdict
from pathlib import Path
from math import prod

input_filename = Path(__file__).stem + ".input"
data = Path(input_filename).read_text()

class mydefaultdict(defaultdict):
    # Always return 10 for missing vals, don't store them
    def __missing__(self, key):
        return 9

heightmap = mydefaultdict()

for y, row in enumerate(data.splitlines()):
    for x, char in enumerate(row):
        heightmap[(x,y)] = int(char)

# Find low points
sum_of_risk = 0
low_points = []
for (x,y), num in heightmap.items():
    if all(num < heightmap[(x1,y1)] 
            for x1,y1 in [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]):
        sum_of_risk += num + 1
        low_points.append((x,y))

print(sum_of_risk)


# Part 2
def find_basin(x, y):
    basin_points = {(x,y)}
    points_to_check = {(x+1,y), (x-1, y), (x, y+1), (x, y-1)}
    while points_to_check:
        point = points_to_check.pop()
        val = heightmap[point]
        if val == 9:
            continue
        else:
            basin_points.add(point)
            x1, y1 = point
            for n_point in {(x1+1,y1), (x1-1, y1), (x1, y1+1), (x1, y1-1)}:
                if n_point in basin_points:
                    continue
                else:
                    points_to_check.add(n_point)
    return basin_points



basins = [find_basin(x, y) for x,y in low_points]
print(f"basin sizes: {[len(basin) for basin in basins]}")
largest_three = list(sorted(len(basin) for basin in basins))[-3:]
print(largest_three)

print(f"{prod(largest_three)}")


