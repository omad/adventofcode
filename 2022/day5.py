import sys
# from collections import deque

with open(sys.argv[1]) as f:
    lines = f.readlines()

stacks = ["" for _ in range(10)]


reading_stacks = True

for line in lines:
    if reading_stacks:
        if line == "\n":
            reading_stacks = False

            stacks_2 = stacks.copy()

            print("Starting with", stacks)
            print("starting with", stacks_2)
            continue

        for stack in range(0, 9):
            column = stack*4 + 1
            if column >= len(line):
                continue
            crate = line[column]
            if crate >= 'A' and crate <= 'Z':
                stacks[stack+1] += crate
    else:
        # Now we're reading instructions!
        _, n, _, f, _, t = line.strip().split()
        n, f, t = int(n), int(f), int(t)
#        print(f"move {n} crates from {f} to {t}")

        crates = stacks[f][:n]
#        print("Moving ", crates)
        # breakpoint()
        stacks[f] = stacks[f][n:]

        stacks[t] = crates[::-1] + stacks[t]
#        print(stacks)
        crates = stacks_2[f][:n]
        stacks_2[f] = stacks_2[f][n:]
        stacks_2[t] = crates + stacks_2[t]

result = [stack[0] for stack in stacks if len(stack) >= 1]

result_2 = [stack[0] for stack in stacks_2 if len(stack) >= 1]
print(stacks)
print(''.join(result))
print()

print(''.join(result_2))