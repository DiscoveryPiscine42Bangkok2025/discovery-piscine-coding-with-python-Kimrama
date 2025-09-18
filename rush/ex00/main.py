from checkmate import checkmate

def main() :
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)
    print("# มีแต่คิง (fail)")
    board2 = """\
..
.K\
"""
    checkmate(board2)  # คาดว่า "Fail"


    print("# 1) Rook ตรงคอลัมน์ (Success)")
    board = """\
.R.
.K.
...\
"""
    checkmate(board)

    print("# 2) Rook มี Pawn ขวาง (Fail)")
    board = """\
RPK
...
...\
"""
    checkmate(board)

    print("# 3) Bishop ทแยงไม่ถูกบล็อก (Success)")
    board = """\
B..
.K.
...\
"""
    checkmate(board)

    print("# 4) Bishop ถูกบล็อกโดย Pawn (Fail)")
    board = """\
B..
.P.
..K\
"""
    checkmate(board)

    print("# 5) Queen โจมตีทแยง (Success)")
    board = """\
Q..
.K.
...\
"""
    checkmate(board)

    print("# 6) Knight โจมตี")
    board = """\
N..
...
.K.\
"""
    checkmate(board)

    print("# 7) Pawn โจมตี (Success)")
    board = """\
...
.K.
P..\
"""
    checkmate(board)

    print("# 8) Pawn ใต้คิงแต่ไม่ทแยง (Fail)")
    board = """\
...
.K.
.P.\
"""
    checkmate(board)

    print("# 9) Invalid 2*3")
    board = """\
R.K
...\
"""
    checkmate(board)

    print("# 10)Invalid 1*3")
    board = """\
R.K\
"""
    checkmate(board)

    print("# 11) Invalid 2*4")
    board = """\
K...
.Q..\
"""
    checkmate(board)

    print("# 12) ไม่มีศัตรู (Fail)")
    board = """\
...
.K.
...\
"""
    checkmate(board)

    print("# 13) Bishop หลัง Rook (Fail)")
    board = """\
....
.K..
..R.
...B\
"""
    checkmate(board)

    print("# 14) Queen หลัง Pawn (Fail)")
    board = """\
.Q.
.P.
.K.\
"""
    checkmate(board)

    print("# 15) Knight  ")
    board = """\
K..
...
.N.\
"""
    checkmate(board)
    
    print("#16) double king (invalid board)")
    board = """\
Q..
.KK
...\
"""
    checkmate(board)

    print("#17) no board")
    board = None
    checkmate(board)

    print("#18) empty board")
    board = """\
"""
    checkmate(board)

    print("#19) 9*9 board")
    board = """\
R........
.K.......
..P......
.........
.........
.........
.........
.........
.........\
"""
    checkmate(board)

if __name__ == "__main__" :
    main()