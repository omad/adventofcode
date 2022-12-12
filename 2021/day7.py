

data = """\
16,1,2,0,4,2,7,1,2,14
"""

from pathlib import Path
data = Path('day7.input').read_text()
nums = [int(n_s) for n_s in data.split(',')]

max_pos = max(nums)

min_cost = 9999999999
for target in range(0, max_pos + 1):
    moves = [abs(target - pos) for pos in nums]
    cost = sum(moves)
    if cost < min_cost:
#        print(f"Picking {target}")
#        print(f"Moves {moves}")
        min_cost = cost

print(f"Part 1: {min_cost}")



min_cost = 9999999999
for target in range(0, max_pos + 1):
    moves = [sum(range(1, abs(target - pos) + 1)) for pos in nums]
    cost = sum(moves)
    if cost < min_cost:
#        print(f"Picking {target}")
#        print(f"Moves {moves}")
        min_cost = cost


print(f"Part 2: {min_cost}")
