from typing import List

def subsetXORSum(nums: List[int]) -> int:
    n = len(nums)
    total_subsets = 1 << n  # 2^n subsets
    xor_sum = 0

    for i in range(total_subsets):
        subset_xor = 0
        for j in range(n):
            if i & (1 << j):  # Check if the j-th bit is set in i
                subset_xor ^= nums[j]
        xor_sum += subset_xor

    return xor_sum