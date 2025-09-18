import math
def check_board_dimension(board: str) -> int:
    dimen = math.sqrt(len(list(board.replace('\n', ''))))
    if dimen != int(dimen):
        print("Error: board is not square")
        exit(1)
    return int(dimen)

def validate_piece(piece: str) -> bool:
    valid_pieces = {'K', 'Q', 'R', 'B', 'P', '.'}
    return piece in valid_pieces

def validate_board(board: str, dimen: int) -> None:
    rows = board.split('\n')
    if len(rows) != dimen:
        print("Error: board does not have the correct number of rows")
        exit(1)
    for row in rows:
        if len(row) != dimen:
            print("Error: row does not have the correct number of columns")
            exit(1)
        for piece in row:
            if not validate_piece(piece):
                print(f"Error: invalid piece '{piece}' found on the board")
                exit(1)

def create_board_matrix(board: str) -> list:
    rows = board.split('\n')
    matrix = [list(row) for row in rows]
    return matrix

def find_king_position(board_matrix: list) -> tuple:
    for i, row in enumerate(board_matrix):
        for j, piece in enumerate(row):
            if piece == 'K':
                return (i, j)
    print("Error: King not found on the board")
    exit(1)

def checkmate(board: str):
    board_dimension = check_board_dimension(board)
    validate_board(board, board_dimension)
    board_matrix = create_board_matrix(board)
    king_position = find_king_position(board_matrix)
    print(board_matrix)
    print(f"Board dimension: {board_dimension}")
    print(f"King position: {king_position}")