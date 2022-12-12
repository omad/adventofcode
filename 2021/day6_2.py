

data = """\
3,4,3,1,2
"""

from pathlib import Path

data = Path('day6.input').read_text()

fishes = [int(n) for n in data.split(',')]

days = 81

def update_fishes(fishes):
    new_fishes = []
    state = []
    for f in fishes:
        if f == 0:
            new_fishes.append(8)
            state.append(6)
        else:
            state.append(f - 1)
    return state + new_fishes


for i in range(days):
#    print(f'Day {i}: {fishes} {len(fishes)}')
    if i in [18, 26, 80]:
        print(f'Day {i}: {len(fishes)}')
    fishes = update_fishes(fishes)
