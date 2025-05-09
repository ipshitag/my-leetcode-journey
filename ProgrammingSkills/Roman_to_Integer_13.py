def romanToInt(s: str) -> int:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    for char in reversed(s):
        current_value = roman_numerals[char]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total

s = "III"
res = romanToInt(s)
print(res) # Output: 3

s = "IV"
res = romanToInt(s)
print(res) # Output: 4

s = "IX"
res = romanToInt(s)
print(res) # Output: 9