import random

def get_dices():
    dices = []
    for _ in range(0, 5):
        dices.append(random.randint(1, 6))
    return dices

def get_score(dices: list):
    dices.sort()

    # best dice
    score = dices[-1] - 1

    # one pair
    for i in range(0, 4):
        if dices[i] == dices[i + 1]:
            score = max(score, 6 + dices[i])

    # two pairs
    for i in range(0, 4):
        if dices[i] == dices[i + 1]:
            for j in range(i + 1, 4):
                if dices[j] == dices[j + 1]:
                    score = max(score, 6 * 6 + dices[j] + dices[i])

    # triple
    for i in range(0, 3):
        if dices[i] == dices[i + 1] == dices[i + 2]:
            score = max(score, 6 * 6 * 6 + dices[i])

    # strit
    tmp = 0
    for i in range(0, 4):
        if dices[i] + 1 == dices[i + 1]:
            tmp += 1
    if tmp == 4:
        score = max(score, 6 * 6 * 6 * 6)

    # full house
    for i in range(0, 4):
        if dices[i] == dices[i + 1]:
            for j in range(i + 2, 3):
                if dices[j] == dices[j + 1] == dices[j + 2]:
                    score = max(score, 6 * 6 * 6 * 6 * 6 + dices[i] * 2 + dices[j] * 3)
    for i in range(0, 3):
        if dices[i] == dices[i + 1] == dices[i + 2]:
            for j in range(i + 3, 4):
                if dices[j] == dices[j + 1]:
                    score = max(score, 6 * 6 * 6 * 6 * 6 + dices[i] * 3 + dices[j] * 2)

    # kare
    for i in range(0, 2):
        if dices[i] == dices[i + 1] == dices[i + 2] == dices[i + 3]:
            score = max(score, 6 * 6 * 6 * 6 * 6 * 6 + dices[i])

    # poker
    i = 0
    if dices[i] == dices[i + 1] == dices[i + 2] == dices[i + 3] == dices[i + 4]:
            score = max(score, 6 * 6 * 6 * 6 * 6 * 6 * 6 + dices[i])

    return score
