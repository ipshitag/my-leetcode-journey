"""
Note:
    This is a simple problem, we just need to check if the robot returns to the origin
    after moving in the given directions.
    The robot can move in 4 directions: U, D, L, R
    U: Up
    D: Down
    L: Left
    R: Right
    
    For every move, we can increase or decrease the values of horizontal and vertical coordinates.
    If the robot returns to the origin, then both values should be 0."""

def judgeCircle(self, moves: str) -> bool:
    # define 2 values, one for horizontal, one for vertical

    h = 0
    v = 0

    for move in moves:
        if move == "U":
            h += 1
        if move == "D":
            h -= 1
        if move == "R":
            v += 1
        if move == "L":
            v -= 1
    if h == 0 and v == 0:
        return True
    return False

moves = "UD"
res = judgeCircle(moves)
print(res)  # Output: True

moves = "LL"
res = judgeCircle(moves)
print(res)  # Output: False

moves = "RRDD"
res = judgeCircle(moves)
print(res)  # Output: False