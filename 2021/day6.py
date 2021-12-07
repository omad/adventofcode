
data = """\
3,4,3,1,2
"""

from pathlib import Path

data = Path('day6.input').read_text()

nums = [int(n) for n in data.split(',')]

population = [0 for i in range(9)]

for n in nums:
    population[n] += 1

print(population)
days = 260

# now iterate
for i in range(1, days):
#    print(f"{i}: {population}")
    prev = population.copy()
    for n in range(8):
        population[n] = prev[n+1]
    population[6] = population[6] + prev[0]
    population[8] = prev[0]

    if i in [18, 80, 256]:
        print(f"{i}: {sum(population)}")
