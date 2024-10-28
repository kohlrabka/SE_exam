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
    n = 100000
    for _ in range(0, n):
        tmp = dice.get_dices()
        assert dice.get_scrore(tmp) == 1