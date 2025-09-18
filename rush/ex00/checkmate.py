def check_board_dimension(board: str) -> int | None:
    rows = board.split("\n")
    n = len(rows)
    if n == 0:
        print("Error")
        return None
    if any(len(row) != n for row in rows):
        print("Error")
        return None
    return n

def normalize_board(board: str) -> str:
    return board.replace(" ", ".")

def validate_piece(piece: str) -> bool:
    return piece in {'K', 'Q', 'R', 'B', 'P', '.'}

def validate_board(board: str, n: int) -> bool:
    rows = board.split("\n")
    king_count = 0
    for row in rows:
        if len(row) != n:
            print("Error")
            return False
        for ch in row:
            if not validate_piece(ch):
                print("Error")
                return False
            if ch == 'K':
                king_count += 1
    if king_count != 1:
        print("Error")
        return False
    return True

def create_board_matrix(board: str) -> list[list[str]]:
    return [list(row) for row in board.split('\n')]

def find_king_position(board_matrix: list[list[str]]) -> tuple[int, int]:
    for r, row in enumerate(board_matrix):
        for c, piece in enumerate(row):
            if piece == 'K':
                return (r, c)

def is_in_bounds(row: int, col: int, n: int) -> bool:
    return 0 <= row < n and 0 <= col < n

def check_pawn(row: int, col: int, king: tuple[int, int], n: int) -> bool:
    for dr, dc in [(-1, -1), (-1, 1)]:
        r, c = row + dr, col + dc
        if is_in_bounds(r, c, n) and (r, c) == king:
            return True
    return False

def check_line(board: list[list[str]], row: int, col: int, king: tuple[int, int], directions: list[tuple[int, int]]) -> bool:
    n = len(board)
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while is_in_bounds(r, c, n):
            if (r, c) == king:
                return True
            if board[r][c] != '.':
                break
            r += dr
            c += dc
    return False

def checkmate(board: str) -> None:
    board = normalize_board(board)
    n = check_board_dimension(board)
    if n is None or not validate_board(board, n):
        return

    board_matrix = create_board_matrix(board)
    king = find_king_position(board_matrix)

    for r in range(n):
        for c in range(n):
            piece = board_matrix[r][c]
            if piece in {'.', 'K'}:
                continue
            if piece == 'P' and check_pawn(r, c, king, n):
                print("Success")
                return
            if piece == 'R' and check_line(board_matrix, r, c, king, [(1,0),(-1,0),(0,1),(0,-1)]):
                print("Success")
                return
            if piece == 'B' and check_line(board_matrix, r, c, king, [(1,1),(1,-1),(-1,1),(-1,-1)]):
                print("Success")
                return
            if piece == 'Q' and check_line(board_matrix, r, c, king, [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]):
                print("Success")
                return

    print("Fail")
