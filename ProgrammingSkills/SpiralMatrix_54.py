from typing import List

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    # Initialize an empty list to store the result
    result = []
    
    # Check if the matrix is empty
    if not matrix:
        return result
    
    # Define the boundaries of the matrix
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    
    # Loop until the boundaries overlap
    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Check if there are remaining rows to traverse
        if top <= bottom:
            # Traverse from right to left along the bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Check if there are remaining columns to traverse
        if left <= right:
            # Traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result