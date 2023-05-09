score = int(input())
for tries in range(score // 5 + 1):
    for transf in range(tries + 1):
        score_wo_drops = 5 * tries + 2 * transf
        if (score - score_wo_drops) % 3 == 0 and score_wo_drops <= score:
            print(tries, transf, (score - score_wo_drops) // 3)
