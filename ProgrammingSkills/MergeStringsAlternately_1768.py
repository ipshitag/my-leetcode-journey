"""
Notes:
Two flags are used to track the current index of each string.
The while loop continues until one of the strings is fully traversed.
The remaining characters of the longer string are appended to the merged list.
One by one character from each string is added to the merged list.

What did not work:
If I do i<j or j<i, it will not work, as it gets only to one string, also the last character of the string is not added to the merged list.

What I learned:
Indexing of strings works like arrays, so I can use the same logic as I would with arrays.
I can use the append method to add the remaining characters of the longer string to the merged list.
The join method can be used to convert the list of characters back to a string, I initially thought to use something like str(merged), but that would not work as it would convert the list to a string representation, not the actual string.

Time complexity:
O(N+M) 
Where N is the length of word1 and M is the length of word2.
The time complexity is O(N+M) because we are iterating through both strings once, and the operations inside the loop are O(1).

Space complexity:
O(N+M) 
Where N is the length of word1 and M is the length of word2.
The space complexity is O(N+M) because we are storing the merged string in a list, which takes up space proportional to the total length of both strings.
"""

def mergeAlternately(self, word1: str, word2: str) -> str:
    #flags for word1 and word2
    i = 0
    j = 0

    #list to save the result string
    merged = []

    #run look till one of the strings ends
    while i < len(word1) and j < len (word2):
        #take one char from each and put it in
        merged.append(word1[i])
        merged.append(word2[j])

        #shift flags forward
        i = i + 1
        j = j + 1

    #check which string is still left
    if i < len(word1):
        #append remaining
        merged.append(word1[i:])
    if j < len(word2):
        merged.append(word2[j:])

    #convert to string
    res = "".join(merged)

    return res

word1 = "abc"
word2 = "pqr"
res = mergeAlternately(word1, word2)
# expected: "apbqcr"
print(res)

word1 = "ab"
word2 = "pqrs"
res = mergeAlternately(word1, word2)
# expected: "apbqrs"
print(res)

word1 = "abcd"
word2 = "pq"
res = mergeAlternately(word1, word2)
# expected: "apbqcd"
print(res)