def climbStairs(n: int) -> int:
    """
    Given an integer n, return the number of distinct ways to climb to the top of the staircase.
    Each time you can either climb 1 or 2 steps. In other words, you can take either a single step or a double step.
    """
    if n <= 2:
        return n
    first = 1
    second = 2
    for i in range(3, n + 1):
        first, second = second, first + second
    return second