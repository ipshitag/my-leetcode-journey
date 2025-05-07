from typing import List

def plusOne(digits: List[int]) -> List[int]:
    num = 0
    for i in range(len(digits)):
        num = num * 10 + digits[i]

    num += 1
    result = []
    while num > 0:
        result.append(num % 10)
        num //= 10
    result.reverse()
    return result

digits = [1,2,3]
res = plusOne(digits)
print(res) 

digits = [4,3,2,1]
res = plusOne(digits)
print(res)

digits = [9]
res = plusOne(digits)
print(res)