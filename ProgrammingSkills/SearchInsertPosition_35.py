from typing import List
def searchInsert(self, nums: List[int], target: int) -> int:
    """
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    """
    # Initialize left and right pointers
    left, right = 0, len(nums) - 1

    # Binary search
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If not found, return the insertion point
    return left