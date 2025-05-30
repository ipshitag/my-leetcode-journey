# Solution
def minimumRecolors(self, blocks: str, k: int) -> int:
    n = len(blocks)
    if n == 0 or k == 0:
        return 0
    if n < k:
        return -1
    min_recolors = float('inf')
    for i in range(n - k + 1):
        recolors = 0
        for j in range(i, i + k):
            if blocks[j] == 'W':
                recolors += 1
        min_recolors = min(min_recolors, recolors)
    return min_recolors