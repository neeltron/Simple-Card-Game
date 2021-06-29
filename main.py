# It's a simple card game in python where two players have to draw one card each and the player whose card has the higher value wins

import random

cards = ['13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']

random.shuffle(cards)

p1 = int(input("Player 1: "))
p2 = int(input("Player 2: "))

c1 = cards[p1]
c2 = cards[p2]

print("Card picked by Player 1: " + c1)
print("Card picked by Player 2: " + c2)

if c1 > c2:
  print("Player 1 is the winner!")
elif c1 < c2:
  print("Player 2 is the winner!")
else:
  print("It's a tie!")
