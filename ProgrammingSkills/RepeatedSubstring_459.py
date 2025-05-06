"""
Note:
This function checks whether a given string can be constructed by repeating a substring of itself.

How it works:
- The trick uses string concatenation and searching:
    1. Concatenate the string to itself, i.e., `s + s`.
    2. Remove the first and last character from this doubled string, i.e., take `[1:-1]`. 
    3. If the original string `s` exists **anywhere** inside this new string, then `s` is a repeated substring pattern. 
        - This is because if `s` could be split into `k` repeats of substring `t`, then rotating `s` any number of times would generate the same pattern, and `s` would definitely appear inside `(s + s)[1:-1]`.
    4. If `s` does not exist in this sliced string, such a repeated pattern is not possible.

Time Complexity: O(N), where N is the length of the string, because the `in` operation for substring has O(N) complexity.
Space Complexity: O(N), because creating (s + s)[1:-1] requires additional memory proportional to the size of the input string.
"""

def repeatedSubstringPattern(s: str) -> bool:
    return s in (s + s)[1:-1]

s = "abab"
res = repeatedSubstringPattern(s)
print(res)  # expected: True
