def lengthOfLastWord(s: str) -> int:
    lst = s.split()
    if not lst:
        return 0
    return len(lst[-1])