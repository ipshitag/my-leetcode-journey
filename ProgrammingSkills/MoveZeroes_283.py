"""
Note:
    This is a LeetCode problem. The problem statement is as follows:
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.

    The solution would be to create a new list and append all non-zero elements to it, then append all zeroes at the end, but that would not be in-place.
    Hence, we will use the two-pointer technique to solve this problem in-place.
    First, we will count the number of zeroes in the array.
    Then, we will iterate through the array and remove the first occurrence of 0 and append it to the end of the list.
    This will ensure that all non-zero elements are in their original order and all zeroes are at the end of the list.
    
    Space complexity is O(1) because we are not using any extra space.
    Time complexity is O(n) because we are iterating through the array once to count the number of zeroes and then again to remove them.
"""

from typing import List

def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        print(zero_count)  # Debug statement to show the count of zeroes
        for _ in range(zero_count):
            nums.remove(0)  # Remove the first occurrence of 0
            nums.append(0) # Append 0 to the end of the list

        print(nums)  # Debug statement to show the modified list after moving zeroes

nums = [0,1,0,3,12]
moveZeroes(nums)

nums = [3,12]
moveZeroes(nums)