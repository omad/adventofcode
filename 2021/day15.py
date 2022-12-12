

data = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

from pathlib import Path
data = Path('day15.input').read_text()


def adjacent(point):
    y,x = point
    yield y-1,x
    yield y+1,x
    yield y,x-1
    yield y,x+1


costs = {}

for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        costs[(y,x)] = int(c)



max_x = max(x for _,x in costs.keys())
max_y = max(y for y,_ in costs.keys())

shortest_path_set = set()
distances = {key:999999999 for key in costs.keys()}

distances[(0,0)] = 0

while len(shortest_path_set) < len(costs):

    # pick vertex
    min_distance = 99999

    for vertex, distance in distances.items():
        if distance < min_distance and vertex not in shortest_path_set:
            min_distance = distance
            min_vertex = vertex

#    print(f"solving {min_vertex}")
    # Add to solved
    shortest_path_set.add(min_vertex)

    if min_vertex == (max_y, max_x):
        break

    min_vertex_cost = distances[min_vertex]
    for point in adjacent(min_vertex):
        if point in costs:
            # if the sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.
            if min_vertex_cost + costs[point] < distances[point]:
                distances[point] = min_vertex_cost + costs[point]

print(distances[(max_y, max_x)])




