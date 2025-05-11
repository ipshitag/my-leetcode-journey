from typing import List

def tictactoe(self, moves: List[List[int]]) -> str:
    """
    :type moves: List[List[int]]
    :rtype: str
    """
    # Initialize the board
    board = [[''] * 3 for _ in range(3)]
    
    # Fill the board with moves
    for i, move in enumerate(moves):
        player = 'A' if i % 2 == 0 else 'B'
        board[move[0]][move[1]] = player
    
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    
    # Check for draw or pending moves
    if len(moves) < 9:
        return 'Pending'
    
    return 'Draw'