"""
Note:
    This is a dynamic programming problem.
    The number of ways to reach the nth step is the sum of the number of ways to reach the (n-1)th step and the (n-2)th step.
    This is because you can reach the nth step by taking a single step from (n-1)th step or a double step from (n-2)th step.
    So, we can use a bottom-up approach to solve this problem.

    Space Complexity:
    O(1) because we are using only two variables to store the number of ways to reach the (n-1)th and (n-2)th steps.

    Time Complexity:
    O(n) because we are iterating from 3 to n to calculate the number of ways to reach the nth step.
"""
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    first = 1
    second = 2
    for i in range(3, n + 1):
        first, second = second, first + second
    return second