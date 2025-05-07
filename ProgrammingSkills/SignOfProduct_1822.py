"""
Note:
    This is a LeetCode problem. The problem statement is as follows:
    Given an integer array nums, return 1 if the product of all the numbers in the array is positive.
    Return -1 if the product of all the numbers in the array is negative.
    Return 0 if the product of all the numbers in the array is zero.

    Pretty simple problem, but I will try to solve it in a more efficient way.
    The naive solution would be to calculate the product of all the numbers in the array and then check if it is positive, negative or zero.

    Space complexity is O(1) because we are not using any extra space.
    Time complexity is O(n) because we are iterating through the array once to calculate the product.
"""


from typing import List

def arraySign(nums: List[int]) -> int:
        product = 1

        for k in nums:
            product = product * k

        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        

nums = [-1,-2,-3,-4,3,2,1]
res = arraySign(nums)
print(res)

nums = [1,5,0,2,-3]
res = arraySign(nums)
print(res)

nums = [-1,1,-1,1,-1]
res = arraySign(nums)
print(res)