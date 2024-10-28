import dice

def test_dices_random():
    n = 1000000
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
