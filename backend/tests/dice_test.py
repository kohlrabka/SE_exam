from backend import dice

def test_dices_random():
    n = 100000
    number_probability = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }
    for _ in range(0, n):
        tmp = dice.get_dices()
        for i in range(0, 5):
            number_probability[str(tmp[i])] += 1
    for key in number_probability:
        assert abs(number_probability[key] / (n * 6) - 1 / 6) < 0.03

def test_dices_score():
    dices = [1, 2, 3, 4, 6]
    assert dice.get_score(dices) == 5

    dices = [1, 1, 2, 3, 4]
    assert dice.get_score(dices) == 6 + 1

    dices = [1, 2, 2, 3, 4]
    assert dice.get_score(dices) == 6 + 2

    dices = [1, 2, 4, 6, 6]
    assert dice.get_score(dices) == 6 + 6

    dices = [1, 5, 4, 5, 6]
    assert dice.get_score(dices) == 6 + 5

    dices = [4, 5, 4, 5, 6]
    assert dice.get_score(dices) == 6 * 6 + 4 + 5

    dices = [4, 3, 4, 6, 6]
    assert dice.get_score(dices) == 6 * 6 + 4 + 6

    dices = [1, 1, 1, 3, 4]
    assert dice.get_score(dices) == 6 * 6 * 6 + 1

    dices = [1, 1, 5, 3, 1]
    assert dice.get_score(dices) == 6 * 6 * 6 + 1

    dices = [1, 4, 5, 4, 4]
    assert dice.get_score(dices) == 6 * 6 * 6 + 4

    dices = [1, 2, 3, 4, 5]
    assert dice.get_score(dices) == 6 * 6 * 6 * 6

    dices = [2, 3, 4, 5, 6]
    assert dice.get_score(dices) == 6 * 6 * 6 * 6

    dices = [1, 4, 1, 4, 4]
    assert dice.get_score(dices) == 6 * 6 * 6 * 6 * 6 + 1 * 2 + 4 * 3

    dices = [2, 5, 2, 5, 5]
    assert dice.get_score(dices) == 6 * 6 * 6 * 6 * 6 + 2 * 2 + 5 * 3

    dices = [2, 5, 5, 5, 5]
    assert dice.get_score(dices) == 6 * 6 * 6 * 6 * 6 * 6 + 5

    dices = [6, 6, 6, 6, 6]
    assert dice.get_score(dices) == 6 * 6 * 6 * 6 * 6 * 6 * 6 + 6