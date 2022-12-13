import sys
from collections import defaultdict

def readinput(fname):
    with open(fname) as f:
        lines = f.readlines()

    trees = defaultdict(int)

    max_y = len(lines)

    for y, line in enumerate(lines):
        line = line.strip()
        max_x = len(line)
        for x, c in enumerate(line):
            trees[(x, y)] = int(c)

    return max_x, max_y, trees

def get_multiple(d, start, end):
    sx, sy = start
    ex, ey = end
    return [d[(x, y)] 
            for x in range(sx, ex)
            for y in range(sy, ey)]



def part_1(max_x, max_y, trees):
    def isvisible(x, y):
        val = trees[(x, y)]
        if x == 0 or y == 0 or x == max_x-1 or y == max_y-1:
            return True
        if val > max(get_multiple(trees, (0, y), (x, y+1))):
            return True
        elif val > max(get_multiple(trees, (x+1, y), (max_x+1, y+1))):
            return True
        elif val > max(get_multiple(trees, (x, 0), (x+1, y))):
            return True
        elif val > max(get_multiple(trees, (x, y+1), (x+1, max_y+1))):
            return True
        else:
            return False

    num_visible = 0

    print(f'mx {max_x}, my {max_y}')
    for x in range(max_x):
        for y in range(max_y):
            print(x, y, end='')
            if isvisible(x, y):
                print(x, y, trees[x, y], end='')
                num_visible += 1
            print()

    print(num_visible)

def part_2(max_x, max_y, trees):
    print("x y l r u d score")
    def viewdistance(x, y):
        val = trees[x, y]
        if x == 0 or y == 0 or x == max_x or y == max_y:
            return 0
        right = 0
        for n, i in enumerate(range(x+1, max_x), start=1):
            right = n
            if trees[(i, y)] >= val:
                break
        left = 0
        for n, i in enumerate(range(x-1, -1, -1), start=1):
            left = n
            if trees[(i, y)] >= val:
                break
        up = 0
        for n, i in enumerate(range(y-1, -1, -1), start=1):
            up = n
            if trees[(x, i)] >= val:
                break
        down = 0
        for n, i in enumerate(range(y+1, max_y), start=1):
            down = n
            if trees[(x, i)] >= val:
                break
        score = left * right * up * down
        if score > 0:
            print(x, y, left, right, up, down, score)
        return score

    best = 0
    bx, by = 0, 0
    for x in range(1, max_x):
        for y in range(1, max_y):
            scenic_score = viewdistance(x, y)
            if scenic_score > best:
                best = scenic_score
                bx, by = x, y
    print(bx, by)
    print(best)


if __name__ == "__main__":
    max_x, max_y, trees = readinput(sys.argv[1])
    part_2(max_x, max_y, trees)

