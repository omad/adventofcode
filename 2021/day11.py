
data = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

# data = """\
# 11111
# 19991
# 19191
# 19991
# 11111
# """

from pathlib import Path

input_filename = Path(__file__).stem + ".input"
print("Reading from: " + input_filename)
data = Path(input_filename).read_text()

cavern = {}

y_max = len(data.splitlines())

def adjacent_points(y, x):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == 0 == j:
                continue
            else:
                yield y+i, x+j


for y, line in enumerate(data.splitlines()):
    x_max = len(line)
    for x, c in enumerate(line):
        cavern[(y,x)] = int(c)

def print_state(cavern):
    for y in range(y_max):
        for x in range(x_max):
            n = cavern[(y,x)]
            if n == 0:
                print("\033[1m" + str(n) + "\033[0m", end='')
            else:
                print(cavern[(y,x)], end='')
        print()
    print()

print_state(cavern)
flashes = 0
# Play game
for i in range(1, 10000+1):

    has_flashed = set()
    # Increase energy level of all by 1
    for k, v in cavern.items():
        cavern[k] = v+1

    need_to_check = True
    while need_to_check:
        need_to_check = False

        for k, v in cavern.items():
            if v > 9:
                if k not in has_flashed:
                    has_flashed.add(k)
                    need_to_check = True
                    for neighbour in adjacent_points(*k):
                        if neighbour in cavern:
                            cavern[neighbour] += 1



    for k in has_flashed:
        cavern[k] = 0
        if i < 101:
            flashes += 1
        

    if len(has_flashed) == len(cavern):
        print(f"Synced after {i}")
        print_state(cavern)
        break

#    print(f"After step {i}")
#    print_state(cavern)

print(flashes)


