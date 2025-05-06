"""
Note:
This function checks whether two strings are anagrams of each other.

How it works:
- An anagram requires both strings to have the same characters with the same frequencies.
- First, the function checks if the lengths of both strings are equal. If not, they're not anagrams.
- If the lengths match, the function uses Python's `collections.Counter` to count the frequency of each character in both strings.
- If the two Counter objects are equal, the strings contain identical characters with identical frequencies → they are anagrams.

Example:
- s = "listen", t = "silent"
    Counter(s) = {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}
    Counter(t) = {'s':1, 'i':1, 'l':1, 'e':1, 'n':1, 't':1}
    Both counters are equal → return True.

Time Complexity: O(N), where N is the length of the strings (since counting the characters is O(N), and Counter equality comparison is also O(N)).
Space Complexity: O(1) if we assume a fixed character set (e.g., lowercase letters). Otherwise, O(N) in the general case as new keys may be created in the Counter.
"""

from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if (Counter(s)) == (Counter(t)):
        return True
    else:
        return False

s = "anagram"
t = "nagaram"
res = isAnagram(s, t)
print(res)  # expected: True

s = "rat"
t = "car"
res = isAnagram(s, t)
print(res)  # expected: False

s = "aa"
t = "bb"
res = isAnagram(s, t)
print(res)  # expected: False