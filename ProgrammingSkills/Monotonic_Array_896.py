from typing import List

def isMonotonic(nums: List[int]) -> bool:
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))
        
nums = [1,2,2,3]
res = isMonotonic(nums)
print(res) # Output: True   

nums = [6,5,4,4]
res = isMonotonic(nums)
print(res) # Output: True

nums = [1,3,2]
res = isMonotonic(nums)
print(res) # Output: False


#### NOTE ####
# Following code did not work.. it gave None
    # Increasing = False
    # Decreasing = False

    # if nums[0] <= nums[1]:
    #     Increasing = True
    # elif nums[0] >= nums[1]:
    #     Decreasing = True

    # for i in range(1, len(nums) - 1):
    #     if Increasing and nums[i] > nums[i + 1]:
    #         return False
    #     elif Decreasing and nums[i] < nums[i + 1]:
    #         return False
    #     else:
    #         pass
