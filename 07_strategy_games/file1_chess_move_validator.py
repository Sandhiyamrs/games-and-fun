# Basic chess move validator (no castling, no en-passant, no promotions)
COLS = "abcdefgh"

def pos_to_coords(pos):
    col = COLS.index(pos[0])
    row = int(pos[1]) - 1
    return row, col

def on_board(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def is_valid_move(piece, frm, to, color="white"):
    r1, c1 = pos_to_coords(frm)
    r2, c2 = pos_to_coords(to)
    dr, dc = r2 - r1, c2 - c1

    if not on_board(r1, c1) or not on_board(r2, c2):
        return False

    piece = piece.lower()
    if piece == "king":
        return max(abs(dr), abs(dc)) == 1
    if piece == "queen":
        return (dr == 0 or dc == 0 or abs(dr) == abs(dc))
    if piece == "rook":
        return dr == 0 or dc == 0
    if piece == "bishop":
        return abs(dr) == abs(dc)
    if piece == "knight":
        return (abs(dr), abs(dc)) in [(1,2),(2,1)]
    if piece == "pawn":
        # basic pawn (no captures, no double-step or en-passant) direction depends on color
        direction = 1 if color == "white" else -1
        return dc == 0 and dr == direction
    return False

if __name__ == "__main__":
    tests = [
        ("knight","g1","f3"),
        ("bishop","c1","g5"),
        ("rook","a1","a8"),
        ("queen","d1","h5"),
        ("pawn","e2","e3")
    ]
    for piece, frm, to in tests:
        print(f"{piece} {frm}->{to}: {is_valid_move(piece, frm, to)}")

