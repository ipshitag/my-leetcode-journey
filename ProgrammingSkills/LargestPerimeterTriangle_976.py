"""
Note:
This is based on the triangle inequality theorem, which states that the sum of the lengths of any two sides of a triangle must be greater than the length of the third side.
This theorem is important because it helps us determine whether three lengths can form a triangle or not, If this condition is not satisfied, you cannot make a triangle with those side lengths; you can't "close" the triangle.
"""

from typing import List
def largestPerimeter(self, nums: List[int]) -> int:
    """
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, 
    formed by any three different indices i, j, and k in nums.
    """
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            return nums[i] + nums[i + 1] + nums[i + 2]
    return 0