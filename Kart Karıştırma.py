# Python program to shuffle a deck of card using the module random
# and draw 5 cards

# import modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ["Spade", "Hearth", "Diamond", "Club"]))


# shuffle the cards
random.shuffle(deck)


for i in range (0, len(deck)):
    print(deck[i])


# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])

