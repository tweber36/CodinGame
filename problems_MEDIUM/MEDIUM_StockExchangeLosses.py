import sys
import time

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
vs = input()

prices = [int(n) for n in vs.split()]


def calculate_max_loss(prices, loss=0):
    """
    Fonction récursive qui:
    _ Cherche le minimum
    _ Coupe la liste en 2 à cet endroit
    _ Calcule le plus grand écart sur la partie gauche et compare avec les écarts précédents pour garder le pire
    _ Renvoie cette fonction sur la partie droite, avec le plus gros écart en paramèetre
    """

    min_price = min(prices) # On cherche le minimum de la liste

    if len(prices) <= 1:
        # Si la liste ne contient plus qu'un élément, on arrête la récursivité
        return min(loss, 0)
    elif prices.index(min_price) == 0:
        # Si le minimum est à gauche, on recalcule sans cet élément
        # (puisqu'on trouvera forcément un meilleur écart ou égal)
        return calculate_max_loss(prices[1:], loss)
    elif prices.index(min_price) == len(prices) - 1:
        # Si le minimum est à droite, on n'a plus besoin de couper la liste en 2, on renvoie le min - max
        return min(loss, 0, min_price-max(prices))
    else:
        # Cas normal, minimum au milieu
        llist = prices[:prices.index(min_price)]
        rlist = prices[prices.index(min_price)+1:]
        return calculate_max_loss(rlist, min(0, loss, min_price - max(llist)))

debut = time.time()
loss = calculate_max_loss(prices)
fin = time.time()
print(fin - debut, file=sys.stderr)
print(loss)
