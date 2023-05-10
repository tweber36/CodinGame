n = int(input())  # the number of adjacency relations
relations = {}
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    if xi not in relations.keys():
        relations[xi] = []
    if yi not in relations.keys():
        relations[yi] = []
    relations[xi].append(yi)
    relations[yi].append(xi)


def graph_center_distance(tree, dist=0):
    """
    Calculate the distance of the center of the graph by eliminating
    the extremities at each step and memoizing the distance made so far.
    :param tree: Dict of the relations remaining at each step (first iteration it's all relations)
    :param dist: Number to remember the distance
    :return: Return either another iteration with smaller tree or final distance
    """
    if len(tree) > 2:
        # We eliminate the extremities with only one adjacency relation from the tree
        # and update the other nodes accordingly
        tree = {k: [x for x in v if len(tree[x]) > 1] for k, v in tree.items() if len(v) > 1}
    elif len(tree) == 2:
        return dist + 1
    elif len(tree) == 1:
        return dist

    return graph_center_distance(dict(tree), dist + 1)


print(graph_center_distance(dict(relations)))
