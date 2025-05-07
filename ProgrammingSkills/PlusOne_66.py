"""
Note:
    This is a LeetCode problem. The problem statement is as follows:
    Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
    The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
    You may assume the integer does not contain any leading zero, except for the number 0 itself.

    We used to do this in 12th, nostalgia!
    The idea is to convert the array into an integer, increment it by one, and convert it back into an array. 
    Multiplying by 10 and adding the digit is a common way to convert an array of digits into an integer.
    Modulo and integer division are used to convert the integer back into an array of digits.
    
    Space complexity is O(1) because we are not using any extra space.
    Time complexity is O(n) because we are iterating through the array once to convert it into an integer.
"""

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