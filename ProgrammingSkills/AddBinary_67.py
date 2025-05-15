def addBinary(self, a: str, b: str) -> str:
    """
    Given two binary strings a and b, return their sum as a binary string.
    """
    # Initialize the result string and carry
    result = []
    carry = 0

    # Reverse the strings to make addition easier
    a = a[::-1]
    b = b[::-1]

    # Iterate through both strings
    for i in range(max(len(a), len(b))):
        # Get the current digits or 0 if the string is shorter
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0

        # Calculate the sum of the digits and carry
        total = digit_a + digit_b + carry
        carry = total // 2  # Update carry for next iteration
        result.append(str(total % 2))  # Append the binary digit to result

    # If there's a carry left, append it to the result
    if carry:
        result.append(str(carry))

    # Reverse the result to get the final binary string
    return ''.join(result[::-1])