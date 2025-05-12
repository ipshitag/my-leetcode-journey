"""
Note:
The primary diagonal of a matrix is the diagonal that runs from the top left to the bottom right.
To calculate the sum of the primary diagonal, we can iterate through the matrix and add the elements where the row index is equal to the column index.
The secondary diagonal of a matrix is the diagonal that runs from the top right to the bottom left.
To calculate the sum of the secondary diagonal, we can iterate through the matrix and add the elements where the row index is equal to n - 1 - column index.

Space Complexity:
O(1)

Time Complexity:
O(n)
where n is the number of rows (or columns) in the matrix.   
"""

from typing import List
def diagonalSum(mat: List[List[int]]) -> int:
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    n = len(mat)
    total = 0
    
    # Iterate through the matrix
    for i in range(n):
        # Add the primary diagonal element
        total += mat[i][i]
        
        # Add the secondary diagonal element if it's not the same as the primary
        if i != n - 1 - i:
            total += mat[i][n - 1 - i]
    
    return total