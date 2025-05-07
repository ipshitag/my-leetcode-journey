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