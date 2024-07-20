from code.calc import modify, Calculator


def test_plus():
    assert Calculator(list(modify(["5", "+", "4"]))).calc() == (5 + 4)


def test_minus():
    assert Calculator(list(modify(["5", "-", "2"]))).calc() == (5 - 2)


def test_multiply():
    assert Calculator(list(modify(["5", "*", "4"]))).calc() == (5 * 4)


def test_division():
    assert Calculator(list(modify(["8", "/", "4"]))).calc() == (8 / 4)


def test_bracket():
    assert Calculator(list(modify(["(","5", "+", "4",")","*","4"]))).calc() == (36)


