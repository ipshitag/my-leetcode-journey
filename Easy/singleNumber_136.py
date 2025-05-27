from typing import List

def singleNumber(nums: List[int]) -> int:
    result =0
    for num in nums:
        result ^= num
    
    return result

# Example usage:
if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(singleNumber(nums))  # Output: 4
    nums = [2, 2, 1]
    print(singleNumber(nums))  # Output: 1
    nums = [1]
    print(singleNumber(nums))  # Output: 1