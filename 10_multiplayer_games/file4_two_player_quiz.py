p1 = int(input("Player1 score: "))
p2 = int(input("Player2 score: "))
winner = "Player1" if p1>p2 else "Player2" if p2>p1 else "Draw"
print(f"Winner: {winner}")
