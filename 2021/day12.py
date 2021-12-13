
data = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

data2 = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

data3 = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

from pathlib import Path
from collections import defaultdict, Counter

input_filename = Path(__file__).stem + ".input"
print("Reading from: " + input_filename)
data = Path(input_filename).read_text()


def read_graph(data):
    graph = defaultdict(set)
    for line in data.splitlines():
        start, end = line.split('-')
        graph[start].add(end)
        graph[end].add(start)

    return graph

def can_visit(path, cave):
    if cave == 'start':
        return False
    counts = Counter(c for c in path if c.islower())


def walk_from(path):
    cave = path[-1]
    for next_cave in graph[cave]:
        if next_cave.islower():
            if next_cave == 'end':
                yield path + ['end']
                continue
            if next_cave not in path:
                yield from walk_from(path + [next_cave])
        else:
            yield from walk_from(path + [next_cave])

graph = read_graph(data)
print(graph)


paths = list(walk_from(['start']))
print(len(paths))

def can_visit(path, cave):
#    print(f"can_visit({path}, {cave}) = ", end="")
    if cave == 'start':
        return False
    counts = Counter(c for c in path if c.islower())
    already_double = any(v > 1 for v in counts.values())
    if already_double:
        return cave not in path
    else:
        return True

def walk_from_2(path):
    cave = path[-1]
    for next_cave in graph[cave]:
        if next_cave.islower():
            if next_cave == 'end':
                yield path + ['end']
                continue
            if can_visit(path, next_cave):
#                print("True")
                yield from walk_from_2(path + [next_cave])
#            else:
#                print("False")
        else:
            yield from walk_from_2(path + [next_cave])

paths = list(walk_from_2(['start']))
#for path in paths:
#    print(path)
print(len(paths))
