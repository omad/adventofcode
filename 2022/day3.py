import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

def priority(char):
    assert len(char) == 1
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

result = 0
for line in lines:
    line = line.strip()
    n = len(line)

    first = set(line[:n//2])
    second = set(line[n//2:])
#    assert len(first) == len(second)

    common = first.intersection(second)
    assert len(common) == 1
    common = common.pop()
    result += priority(common)

print(result)


result = 0
for l, u in zip(range(0, len(lines), 3), range(3, len(lines)+1, 3)):
    print(l, u)
    group = [set(li.strip()) for li in lines[l: u]]

    print(group)
    common = group[0].intersection(*group[1:])
    print(common)

    assert len(common) == 1
    common = common.pop()
    print(common)
    result += priority(common)

print(result)
