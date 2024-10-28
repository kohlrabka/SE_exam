import random

def get_dices():
    dices = []
    for _ in range(0, 5):
        dices.append(random.randint(1, 6))
    return dices

def get_scrore(dices):
    return 1
