import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cards1 = []
cards2 = []

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    cards1.append(cardp_1)

m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    cards2.append(cardp_2)

nb_rounds = 0

def greater_than(cardA, cardB):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    idxA = order.index(cardA[:-1])
    idxB = order.index(cardB[:-1])
    if idxA > idxB:
        return True
    else:
        return False


def this_is_war(cards1, cards2, played_1, played_2):
    for i in range(3):
        try:
            played_1.append(cards1.pop(0))
            played_2.append(cards2.pop(0))
        except IndexError:
            print("PAT")
            exit()
    return

print(cards1, cards2, file=sys.stderr)

while cards1 and cards2:
    played_1 = []
    played_2 = []

    played_1.append(cards1.pop(0))
    played_2.append(cards2.pop(0))

    while played_1[-1][:-1] == played_2[-1][:-1]:
        this_is_war(cards1, cards2, played_1, played_2)
        if cards1 and cards2:
            played_1.append(cards1.pop(0))
            played_2.append(cards2.pop(0))
        else:
            print("PAT")
            exit()

    if greater_than(played_1[-1], played_2[-1]):
        cards1.extend(played_1)
        cards1.extend(played_2)
    else:
        cards2.extend(played_1)
        cards2.extend(played_2)

    print(cards1, cards2, file=sys.stderr)

    nb_rounds += 1

if not cards1:
    print("2 %d" % nb_rounds)
elif not cards2:
    print("1 %d" % nb_rounds)

