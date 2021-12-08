

data = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

from pathlib import Path
input_filename = Path(__file__).stem + ".input"
data = Path(input_filename).read_text()

entries = [
    line.split(' | ')
    for line in data.strip().splitlines()
]

entries = [
    (
        [frozenset(s) for s in signal_patterns.split()], 
        [frozenset(s) for s in output_values.split()]
    )
    for signal_patterns, output_values in entries
]

count = 0

for _, output_values in entries:
    for val in output_values:
        if len(val) in (2, 3, 4, 7):
            count += 1

print(count)


def derive_mappings(patterns):
    mapping = {}
    mapping[1] = [pat for pat in patterns if len(pat) == 2][0]
    mapping[4] = [pat for pat in patterns if len(pat) == 4][0]
    mapping[7] = [pat for pat in patterns if len(pat) == 3][0]
    mapping[8] = [pat for pat in patterns if len(pat) == 7][0]
    six_long = set(pat for pat in patterns if len(pat) == 6)
    five_long = set(pat for pat in patterns if len(pat) == 5)
    mapping[9] = [pat for pat in six_long if pat >= mapping[4]][0]
    six_long.remove(mapping[9])
    mapping[0] = [pat for pat in six_long if pat >= mapping[1]][0]
    six_long.remove(mapping[0])
    mapping[6] = list(six_long)[0]

    mapping[3] = [pat for pat in five_long if pat >= mapping[1]][0]
    five_long.remove(mapping[3])
    mapping[5] = [pat for pat in five_long if pat <= mapping[6]][0]
    five_long.remove(mapping[5])
    mapping[2] = list(five_long)[0]

    mapping = {v: k for k, v in mapping.items()}
    return mapping



total = 0
for patterns, values in entries:
    mapping = derive_mappings(patterns)

    output_value = int("".join(str(mapping[val]) for val in values))
    total += output_value


print(total)



