def multiply(self, num1: str, num2: str) -> str:
    """
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
    """
    # Edge case: if either number is "0", the product is "0"
    if num1 == "0" or num2 == "0":
        return "0"

    # Initialize the result array to store intermediate products
    result = [0] * (len(num1) + len(num2))

    # Reverse both numbers for easier multiplication
    num1 = num1[::-1]
    num2 = num2[::-1]

    # Multiply each digit of num1 with each digit of num2
    for i in range(len(num1)):
        for j in range(len(num2)):
            # Multiply the digits and add to the corresponding position in result
            product = int(num1[i]) * int(num2[j])
            result[i + j] += product

            # Handle carry over
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    # Remove leading zeros and convert result to string
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))  # Reverse back to original order and convert to string