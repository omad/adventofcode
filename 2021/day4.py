
data = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


from pathlib import Path

input_filename = Path(__file__).stem + ".input"
print("Reading from: " + input_filename)
data = Path(input_filename).read_text()

data = data.splitlines()
drawn_nums = [v for v in data[0].split(',')]

boards = []
for start_row in range(2, len(data), 6):
    board = [row.split() 
            for row in data[start_row:start_row + 5]]
    boards.append(board)

def is_winner(board):
    for x in range(5):
        if all(val == "*" for val in board[x]):
            return True
    for y in range(5):
        col = [row[y] for row in board]
        if all(val == "*" for val in col):
            return True
    return False

def board_sum(board):
    total = 0
    for row in board:
        for val in row:
            if val != "*":
                total += int(val)
    return total

# Now play!
def play(boards, drawn_nums):
    found_first = False
    for num in drawn_nums:
        boards = [[["*" if val == num else val
            for val in row]
            for row in board]
            for board in boards]

        # Check
        for i, board in enumerate(boards):
            if is_winner(board):
                boards.pop(i)
                if found_first == False:
                    score = int(num) * board_sum(board)
                    print(f"Part 1: {score}")
                elif found_first == True and len(boards) == 0:
                    score = int(num) * board_sum(board)
                    print(f"Part 2: {score}")
                found_first = True
score = play(boards, drawn_nums)

print(score)

