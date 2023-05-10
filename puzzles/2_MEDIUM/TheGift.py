"""
If the budget for one person in under the mean contribution for every remaining participant
then his contribution will be his maximum budget.
Otherwise the contribution is equal to the mean contribution.
"""
n = int(input())    # Number of participants
c = int(input())    # The contribution to reach

budgets = []    # Maximum budget of each participant
contributions = []  # Contributions made by each participant

for i in range(n):
    b = int(input())
    budgets.append(b)

if sum(budgets) < c:
    print("IMPOSSIBLE")
else:
    budgets.sort()
    while len(budgets) > 0:
        remaining_mean = int((c - sum(contributions)) / len(budgets))
        if budgets[0] <= remaining_mean:
            contributions.append(budgets[0])
        else:
            contributions.append(remaining_mean)
        del budgets[0]
    for i in contributions:
        print(i)
