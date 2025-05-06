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