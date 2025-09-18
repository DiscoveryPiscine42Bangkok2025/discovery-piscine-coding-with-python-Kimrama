import math

def check_board_dimension(board: str) -> int:
    size = len(board.replace('\n', ''))
    dimen = math.isqrt(size)
    if dimen * dimen != size:
        print("Error")
        return None
    return dimen

def validate_piece(piece: str) -> bool:
    return piece in {'K', 'Q', 'R', 'B', 'P', '.'}

def validate_board(board: str, dimen: int) -> bool:
    rows = board.split('\n')
    if len(rows) != dimen:
        print("Error")
        return False
    for row in rows:
        if len(row) != dimen:
            print("Error")
            return False
        if any(not validate_piece(ch) for ch in row):
            print("Error")
            return False
    return True

def create_board_matrix(board: str) -> list[list[str]]:
    return [list(row) for row in board.split('\n')]

def find_king_position(board_matrix: list[list[str]]) -> tuple[int, int] | None:
    for i, row in enumerate(board_matrix):
        for j, piece in enumerate(row):
            if piece == 'K':
                return (i, j)
    print("Error")
    return None

def is_in_bounds(x: int, y: int, n: int) -> bool:
    return 0 <= x < n and 0 <= y < n


def check_pawn(x: int, y: int, king: tuple[int, int]) -> bool:
    for dx, dy in [(-1, -1), (-1, 1)]:
        if (x + dx, y + dy) == king:
            return True
    return False

def check_line(board: list[list[str]], x: int, y: int,
               king: tuple[int, int], directions: list[tuple[int, int]]) -> bool:
    n = len(board)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while is_in_bounds(nx, ny, n):
            if (nx, ny) == king:
                return True
            if board[nx][ny] != '.': 
                break
            nx += dx
            ny += dy
    return False


def checkmate(board: str) -> None:
    n = check_board_dimension(board)
    if n is None or not validate_board(board, n):
        return

    board_matrix = create_board_matrix(board)
    king = find_king_position(board_matrix)
    if king is None:
        return

    for i in range(n):
        for j in range(n):
            piece = board_matrix[i][j]
            if piece == '.' or piece == 'K':
                continue

            if piece == 'P' and check_pawn(i, j, king):
                print("Success")
                return
            if piece == 'R' and check_line(board_matrix, i, j, king,
                                           [(1,0),(-1,0),(0,1),(0,-1)]):
                print("Success")
                return
            if piece == 'B' and check_line(board_matrix, i, j, king,
                                           [(1,1),(1,-1),(-1,1),(-1,-1)]):
                print("Success")
                return
            if piece == 'Q' and check_line(board_matrix, i, j, king,
                                           [(1,0),(-1,0),(0,1),(0,-1),
                                            (1,1),(1,-1),(-1,1),(-1,-1)]):
                print("Success")
                return

    print("Fail")
