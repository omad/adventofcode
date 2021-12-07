
data = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

from pathlib import Path

data = Path('day3.input').read_text()



zeros = []
total = 0

for line in data.splitlines():
    if total == 0:
        zeros = [0] * len(line)
    total += 1
    for i, digit in enumerate(line):
        if digit == "0":
            zeros[i] += 1

swap = str.maketrans({"0":"1", "1":"0"})

half = total / 2
# gamma is most common bit
gamma_str = "".join("0" if val > half else "1" 
                for val in zeros)

gamma_rate = int(gamma_str, base=2)

epsilon_rate = int(gamma_str.translate(swap), base=2)


print(f"Part 1: {gamma_rate * epsilon_rate}")


# oxygen
nums = data.splitlines()
for i in range(len(nums[0])):
    # find most common
    if len([num[i] 
        for num in nums 
        if num[i] == "1"]) >= (len(nums) / 2):
        keep_bit = "1"
    else:
        keep_bit = "0"
    nums = [num for num in nums if num[i] == keep_bit]
    print(f"{i} - {len(nums)}")
    if len(nums) == 1:
        oxygen_rating = int(nums[0], 2)
        break


# CO2
nums = data.splitlines()
for i in range(len(nums[0])):
    if len([num[i] for num in nums if num[i] == "1"]) >= (len(nums) / 2):
        keep_bit = "0"
    else:
        keep_bit = "1"
    nums = [num for num in nums if num[i] == keep_bit]
    if len(nums) == 1:
        co2_rating = int(nums[0], 2)
        break

print(f"Part 2: {oxygen_rating * co2_rating}")

