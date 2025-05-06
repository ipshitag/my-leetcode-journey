def repeatedSubstringPattern(s: str) -> bool:
    """
    Note:
    The idea is to check if the string can be constructed by repeating a substring.
    We can do this by checking if the string is equal to itself concatenated with itself, excluding the first and last characters.
    If the string can be constructed by repeating a substring, then it will appear in the concatenated string.
    
    Space Complexity: O(1)
    Why: Because we are not using any extra space that grows with the input size.
    
    Time Complexity: O(n) where n is the length of s.
    Why: Because we are traversing the string once to check if it is equal to itself concatenated with itself.
    """
    return s in (s + s)[1:-1]

s = "abab"
res = repeatedSubstringPattern(s)
print(res)  # expected: True
