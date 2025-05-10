"""
Note:
    This is a simple problem, we just need to check if the robot returns to the origin
    after moving in the given directions.
    The robot can move in 4 directions: U, D, L, R
    U: Up
    D: Down
    L: Left
    R: Right
    
    If the robot goes up, it should go down the same number of times
    If the robot goes left, it should go right the same number of times
    
    Time complexity: O(N)
    Space complexity: O(1)"""

def judgeCircle(self, moves: str) -> bool:
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
    
        
moves = "UD"
res = judgeCircle(moves)
print(res)  # Output: True

moves = "LL"
res = judgeCircle(moves)
print(res)  # Output: False

moves = "RRDD"
res = judgeCircle(moves)
print(res)  # Output: False