"""
Note:
1. The function countOdds takes two integers, low and high, as input.
2. It checks if low is even or odd and adjusts it to the next odd number if it's even.
3. It checks if high is even or odd and adjusts it to the previous odd number if it's even.
4. Finally, it calculates the count of odd numbers in the range [low, high] using the formula (high - low) // 2 + 1.

Space Complexity:
O(1)

Time Complexity:
O(1)
"""

def countOdds(self, low: int, high: int) -> int:
    # Check if low is even or odd
    if low % 2 == 0:
        low += 1  # Increment low to the next odd number
    # Check if high is even or odd
    if high % 2 == 0:
        high -= 1  # Decrement high to the previous odd number
    # Calculate the count of odd numbers in the range [low, high]
    return (high - low) // 2 + 1