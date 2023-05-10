# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
node_list = {x: set() for x in range(n)}    # dict comprehension to save all the nodes

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    node_list[n1].add(n2)
    node_list[n2].add(n1)

gateways = set()
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.add(ei)

# game loop
while True:
    si = int(input())                   # The index of the node on which the Skynet agent is positioned this turn
    exits = node_list[si] & gateways    # find if the agent si is next to a gateway
    if exits:                           # if it's the case, we cut the link and update the sets of links
        node = exits.pop()
        node_list[si].remove(node)
        node_list[node].remove(si)
        print(si, node) 
    else:                               # if not, we cut a random link next to a gateway
        for gateway in gateways:
            if node_list[gateway]:      # to choose a gateway that still has links
                node = node_list[gateway].pop()
                node_list[node].remove(gateway)
                print(node, gateway)
                break
