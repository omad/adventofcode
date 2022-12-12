from dataclasses import dataclass

import sys


@dataclass(frozen=True)
class Position:
    x: int = 0
    y: int = 0

    def is_touching(self, other):
        ox, oy = other
        return (self.x in [ox - 1, ox, ox + 1]) and (self.y in [oy - 1, oy, oy + 1])

    def __add__(self, other):
        dx, dy = other
        return Position(self.x + dx, self.y + dy)

    def __iter__(self):
        return iter([self.x, self.y])

    def __eq__(self, other):
        ox, oy = other
        return self.x == ox and self.y == oy


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    H = Position(0, 0)
    T = Position(0, 0)

    MOVES = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }

    tail_locs = set()
    tail_locs.add(T)

    for line in lines:
        direction, steps = line.strip().split()
        print(line.strip())
#        if line.strip() == "U 4": breakpoint()
        for _ in range(int(steps)):
            H = H + MOVES[direction]

            # Check and move tail
            if H.is_touching(T):
                print("touching")
                continue
            else:
                if H.x == T.x:
                    if H.y > T.y:
                        T = T + (0, 1)
                    else:
                        T = T + (0, -1)
                elif H.y == T.y:
                    if H.x > T.x:
                        T = T + (1, 0)
                    else:
                        T = T + (-1, 0)
                else: # diagonal
                    T = Position(
                            T.x + 1 * (1 if T.x < H.x else -1),
                            T.y + 1 * (1 if T.y < H.y else -1)
                            )

            print(T)

            tail_locs.add(T)

    print(len(tail_locs))
