from collections import Counter
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Count evens only
        even_counts = Counter([x for x in nums if x % 2 == 0])
        if not even_counts:
            return -1
        # Find max frequency
        max_freq = max(even_counts.values())
        candidates = [num for num, freq in even_counts.items() if freq == max_freq]
        return min(candidates)
