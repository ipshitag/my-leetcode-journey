"""
Note:
Quite simple problem, just use the inbuilt function index() to find the first occurrence of needle in haystack.
The function returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Space Complexity: O(1)
Why: Because we are not using any extra space that grows with the input size.

Time Complexity: O(n) where n is the length of haystack.
Why: Because in the worst case, we have to traverse the entire haystack to find the needle.
"""

def strStr(haystack: str, needle: str) -> int:
    if (needle in haystack):
        return (haystack.index(needle))
    else:
        return -1
    
haystack = "sadbutsad"
needle = "sad"
res = strStr(haystack, needle)
print(res) # Output: 0

haystack = "leetcode"
needle = "leeto"
res = strStr(haystack, needle)
print(res) # Output: -1