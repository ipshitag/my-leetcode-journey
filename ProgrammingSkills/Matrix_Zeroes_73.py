from typing import List
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    row_zero = [False] * rows
    col_zero = [False] * cols

    # First pass: mark the rows and columns that need to be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero[i] = True
                col_zero[j] = True

    # Second pass: set the marked rows and columns to zero
    for i in range(rows):
        for j in range(cols):
            if row_zero[i] or col_zero[j]:
                matrix[i][j] = 0