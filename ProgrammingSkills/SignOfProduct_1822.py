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