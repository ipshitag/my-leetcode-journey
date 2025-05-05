"""
Note:
XOR is used to find the difference between two strings.
XOR is a bitwise operation that takes two bits and returns 1 if the bits are different, and 0 if they are the same.
Working of XOR:
TT = F
FF = F
TF = T  
FT = T

So only the different bit will be 1, and all the same bits will be 0.
Here we are xorring all chanracters, this makes sense because if we have two same characters, they will cancel each other out
A non working solution is below.. but it fails if there is multiple instances of the same character in the string.

The solution has a time complexity of O(N) and a space complexity of O(N), Where N is the length of the string.
"""

def findTheDifference(s: str, t: str) -> str:
    res = 0
    for c in s + t:
        res ^= ord(c)
    return chr(res)

s = "abcd"
t = "abcde"
res = findTheDifference(s, t)
print(res)  # expected: "e"

s = ""
t = "y"
res = findTheDifference(s, t)
print(res)

s = "aa"
t = "a"
res = findTheDifference(s, t)
print(res)


#### NOTE ###
# Didnt work lol
# for strings like aa and a, it should return a, but it returns None
# def findTheDifference(s: str, t: str) -> str:
#     if len(s) == 0:
#         return t[0]
#     if len(t) == 0:
#         return s[0]
#     j = 0
#     if len(s) > len(t):
#         while j < len(s):
#             if s[j] not in t:
#                 return s[j]
#             j += 1
#     else:
#         while j < len(t):
#             if t[j] not in s:
#                 return t[j]
#             j += 1