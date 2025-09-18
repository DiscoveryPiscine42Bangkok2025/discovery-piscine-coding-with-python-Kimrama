from checkmate import checkmate

def print_board(board: str):
    for row in board.split("\n"):
        print(" ".join(row))
    print()

def run_test(name: str, board: str):
    print(f"=== {name} ===")
    print_board(board)
    checkmate(board)
    print()

def main():
    # 1) Pawn check (Success)
    board1 = """\
R...
.K..
..P.
...."""
    run_test("Pawn attacks King (Success)", board1)

    # 2) No check (Fail)
    board2 = """\
R...
.K..
....
...."""
    run_test("No piece attacks King (Fail)", board2)

    # 3) Multiple kings (Error)
    board3 = """\
K...
....
...K
...."""
    run_test("Multiple Kings (Error)", board3)

    # 4) Invalid character (Error)
    board4 = """\
R...
.K..
..X.
...."""
    run_test("Invalid Character (Error)", board4)

    # 5) Not square (Error)
    board5 = """\
R....
.K..
..P.
...."""
    run_test("Not Square Board (Error)", board5)

    # 6) No King (Error)
    board6 = """\
R...
....
....
...."""
    run_test("No King (Error)", board6)

    # 7) Rook attacks King vertically (Success)
    board7 = """\
R...
.K..
R...
...."""
    run_test("Rook attacks King vertically (Success)", board7)

    # 8) Rook attacks King horizontally (Success)
    board8 = """\
...R
.K..
....
...."""
    run_test("Rook attacks King horizontally (Success)", board8)

    # 9) Bishop attacks King (Success)
    board9 = """\
B...
.K..
....
...."""
    run_test("Bishop attacks King (Success)", board9)

    # 10) Queen attacks King diagonally (Success)
    board10 = """\
Q...
.K..
....
...."""
    run_test("Queen attacks King diagonally (Success)", board10)

    # 11) Queen attacks King horizontally (Success)
    board11 = """\
..QK
....
....
...."""
    run_test("Queen attacks King horizontally (Success)", board11)

    # 12) Pawn at top edge (Fail, cannot attack outside board)
    board12 = """\
..P.
.K..
....
...."""
    run_test("Pawn at top edge (Fail)", board12)

    # 13) King surrounded but not attacked (Fail)
    board13 = """\
....
.RK.
.B..
...."""
    run_test("King blocked but not attacked (Fail)", board13)

    # 14) Space normalization (Success)
    board14 = """\
R...
 K..
  P.
....
"""
    run_test("Space normalization (Success)", board14)

    # 15) Empty 1x1 board with King only (Fail, no attackers)
    board15 = "K"
    run_test("Single King only 1x1 (Fail)", board15)

if __name__ == "__main__":
    main()
