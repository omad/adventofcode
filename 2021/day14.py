
data = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


from pathlib import Path
from collections import Counter, defaultdict

input_filename = Path(__file__).stem + ".input"
print("Reading from: " + input_filename)
data = Path(input_filename).read_text()


lines = [line.strip() for line in data.splitlines()]

polymer = template = lines[0]

rules = {}
for line in lines[2:]:
    pair, el = line.split(' -> ')
    rules[pair] = el

for i in range(1, 10 + 1):
    new_polymer = ""
    for j in range(len(polymer) - 1):
        pair = polymer[j:j+2]
        new_polymer += pair[0] + rules.get(pair, '')

    polymer = new_polymer + polymer[-1]
    counted = Counter(polymer).most_common()
    _, most_common = counted[0]
    _, least_common = counted[-1]
    print(i, len(polymer), most_common, least_common, f"{most_common - least_common}")
#    print(f"After step {i}: length={len(polymer)} {polymer}")

letters = Counter(polymer)
polymer = Counter(template[i:i+2] for i in range(len(template)-1))

for i in range(1, 40 + 1):
    new_polymer = defaultdict(int)
    for pair, count in polymer.items():
        for new_pair in [pair[0]+rules[pair], rules[pair]+pair[1]]:
            new_polymer[new_pair] += count
    polymer = new_polymer

counts = [max(sum(count for (p1,_),count in polymer.items() if c == p1),
            sum(count for (_,p2),count in polymer.items() if c == p2))
            for c in set(''.join(polymer.keys()))]

print(max(counts) - min(counts))



