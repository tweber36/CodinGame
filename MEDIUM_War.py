import collections

cards_1 = collections.deque()
cards_2 = collections.deque()
nb_rounds = 0

# Cards for player 1
n = int(input())
cards_1.extend(input() for _ in range(n))

# Cards for player 2
m = int(input())
cards_2.extend(input() for _ in range(m))


def this_is_war(c1, c2, p1, p2):
    """
    Add 4 cards to each played cards from the deck of each player
    :param c1: Deck of cards for player 1
    :param c2: Deck of cards for player 2
    :param p1: List of cards played for player 1
    :param p2: List of cards played for player 2
    :return: nothing because lists are modified directly
    """
    for i in range(4):
        try:
            p1.append(c1.popleft())
            p2.append(c2.popleft())
        except IndexError:
            print("PAT")
            exit()


def greater_than(card1, card2):
    """
    Compare two cards to see which one is higher
    The two cards cannot be of same high (so it is not tested)
    The order is from 2 to 10 then J Q K A
    :param card1: Value of card 1: '3', '10', '7', 'K'
    :param card2: Value of card 2
    :return: True if card1 > card2, False otherwise
    """
    order = list('23456789JQKA')
    order.insert(8, '10')   # because '10' uses two characters
    return order.index(card1) > order.index(card2)


while cards_1 and cards_2:
    # We add the first card of the deck for each player
    # If it's the same value, then there is a "war"
    # Otherwise the higher card wins
    nb_rounds += 1  # New round
    played_1 = [cards_1.popleft()]
    played_2 = [cards_2.popleft()]

    while played_1[-1][:-1] == played_2[-1][:-1]:   # Slicing to remove the suit
        this_is_war(cards_1, cards_2, played_1, played_2)

    if greater_than(played_1[-1][:-1], played_2[-1][:-1]):
        cards_1.extend(played_1)
        cards_1.extend(played_2)
    else:
        cards_2.extend(played_1)
        cards_2.extend(played_2)

if not cards_1:
    print("2 %d" % nb_rounds)
else:
    print("1 %d" % nb_rounds)
