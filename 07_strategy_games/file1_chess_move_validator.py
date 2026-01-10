def rook_move(start, end):
    return start[0] == end[0] or start[1] == end[1]

print("♟️ Chess Move Validator (Rook)\n")

start = (0, 0)
end = (0, 5)

if rook_move(start, end):
    print("Valid move ✔️")
else:
    print("Invalid move ❌")

