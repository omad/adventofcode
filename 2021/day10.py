
data = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


from pathlib import Path

input_filename = Path(__file__).stem + ".input"
print("Reading from: " + input_filename)
data = Path(input_filename).read_text()

data = data.splitlines()

PAIRS = {
    "{": "}",
    "(": ")",
    "<": ">",
    "[": "]",
}

ILLEGAL_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
errors = {
    ")": 0,
    "]": 0,
    "}": 0,
    ">": 0,
}
validlines = []
for line in data:
    stack = []
    valid = True
    for c in line:
        if c in "([{<":
            stack.append(c)
        elif c in ")]}>":
            expected = PAIRS[stack.pop()]
            if c == expected:
                continue
            else:
                print(line)
                print(f"Expected {expected} but found {c}")
                errors[c] += 1
                valid = False
                break
    if valid:
        stack.reverse()
        reqd = [PAIRS[c] for c in stack]
        validlines.append((line, reqd))

print(errors)
score = sum(count * ILLEGAL_SCORES[k] for k, count in errors.items())
print(score)
                
print("Part 2!")

COMPLETION_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

scores = []
for line, reqd in validlines:
    reqd = "".join(reqd)


    score = 0
    for c in reqd:
        score *= 5
        score += COMPLETION_SCORES[c]
    print(f"{line} - Complete by adding {reqd} - Score: {score}")
    scores.append(score)

import statistics

print(f"{statistics.median(scores)}")

