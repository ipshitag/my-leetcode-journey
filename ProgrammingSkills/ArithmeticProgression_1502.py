"""
Note:
    This is a LeetCode problem. The problem statement is as follows:
    Given an array of numbers arr, return true if the numbers can be arranged to form an arithmetic progression, or false otherwise.

    Arithmetic progression is a sequence of numbers in which the difference between any two consecutive elements is the same.
    For example, [1, 3, 5] and [5, 3, 1] are arithmetic progression while [1, 2, 4] and [1, 2, 3] are not.

    To solve this problem, we can sort the array and check if the difference between consecutive elements is the same.
    If the difference is the same for all consecutive elements, then the array can be arranged to form an arithmetic progression.

    We can use the built-in sort function to sort the array and then iterate through the sorted array to check if the difference is the same.

    Space Complexity:
        O(1) - We are not using any extra space except for the input array.
    Time Complexity:
        O(nlogn) - The sort function takes O(nlogn) time and the iteration takes O(n) time.
    where n is the number of elements in the array.
"""

from typing import List
def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True

arr = [3,5,1]
res = canMakeArithmeticProgression(arr)
print(res) # Output: True

arr = [1,2,4]
res = canMakeArithmeticProgression(arr)
print(res) # Output: False