import random

def get_dices():
    dices = []
    for _ in range(0, 5):
        dices.append(random.randint(1, 6))
    return dices

