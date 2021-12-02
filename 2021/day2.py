
sample = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

from pathlib import Path

sample = Path('day2.input').read_text()

steps = [step.split() for step in sample.splitlines()]
steps = [(direction, int(val)) for direction, val in steps]


horiz = depth = 0

for direction, val in steps:
    if direction == 'forward':
        horiz += val
    elif direction == 'up':
        depth -= val
    elif direction == 'down':
        depth += val

print(f"Part 1: {depth * horiz}")


# Part 2

horiz = depth = aim = 0


for direction, val in steps:
    if direction == 'forward':
        horiz += val
        depth += aim * val
    elif direction == 'up':
        aim -= val
    elif direction == 'down':
        aim += val


print(f"Part 2: {depth * horiz}")
