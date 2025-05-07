from typing import List

def arraySign(nums: List[int]) -> int:
    sign = 1

    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            sign = sign * -1

    return sign

nums = [-1,-2,-3,-4,3,2,1]
res = arraySign(nums)
print(res)

nums = [1,5,0,2,-3]
res = arraySign(nums)
print(res)

nums = [-1,1,-1,1,-1]
res = arraySign(nums)
print(res)