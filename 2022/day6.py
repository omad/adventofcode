import sys

with open(sys.argv[1]) as f:
    chars = f.read()


def find_marker(chars, length=4):
    for n in range(length, len(chars)):
        tocheck = chars[n-length:n]
        if len(set(tocheck)) == length:
            return n


print(find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb'))

print(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz'))

print(find_marker(chars))
print(find_marker(chars, length=14))
