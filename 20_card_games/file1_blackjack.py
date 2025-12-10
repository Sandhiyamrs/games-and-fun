# Very simplified blackjack simulation
import random
deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
random.shuffle(deck)
player=[deck.pop(),deck.pop()]
dealer=[deck.pop(),deck.pop()]
print("Dealer shows:", dealer[0])
print("You have:", player, "total", sum(player))
while sum(player)<21 and input("Hit? (y/n): ")=="y":
    player.append(deck.pop()); print("You:", sum(player))
if sum(player)>21:
    print("Bust! You lose.")
else:
    while sum(dealer)<17: dealer.append(deck.pop())
    print("Dealer total:", sum(dealer))
    if sum(dealer)>21 or sum(player)>sum(dealer): print("You win!")
    elif sum(player)==sum(dealer): print("Push")
    else: print("You lose")

