
data = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


from pathlib import Path

input_filename = Path(__file__).stem + ".input"
print("Reading from: " + input_filename)
data = Path(input_filename).read_text()


dots = set()
instructions = []

UPTO_INSTRUCTIONS = False
for line in data.splitlines():
    if UPTO_INSTRUCTIONS:
        axis, coord = line.split()[2].split('=')
        instructions.append((axis, int(coord)))
    elif line.strip() == '':
        UPTO_INSTRUCTIONS = True
    else:
        # Readings dots
        x_s, y_s = line.split(',')
        dots.add((int(x_s), int(y_s)))


for axis, fold_line in instructions:
    dots_n = set()
    for x, y in dots:
        if axis == 'y':
            if y <= fold_line:
                dots_n.add((x, y))
            else:
                dots_n.add((x, fold_line - (y - fold_line)))
        elif axis == 'x':
            if x <= fold_line:
                dots_n.add((x, y))
            else:
                dots_n.add((fold_line - (x - fold_line), y))

        else:
            raise Error(f"Bad axis: {axis}")
    dots = dots_n

print(len(dots_n))

xs, ys = zip(*((x, y) for x, y in dots))
max_x, max_y = max(xs), max(ys)

for y in range(max_y + 1):
    for x in range(max_x + 1):
        if (x, y) in dots:
            print('#', end='')
        else:
            print('.', end='')
    print()





