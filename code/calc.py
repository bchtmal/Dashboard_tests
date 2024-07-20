import queue
from typing import List, Text, Union


def read() -> List[Text]:
    s = input()
    return s.split()


def modify(tokens: List[Text]) -> List[Union[Text, int]]:
    for token in tokens:
        if token.isdigit():
            yield int(token)
        else:
            yield token


class Calculator:
    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }
    map = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    def __init__(self, tokens: List[Union[Text, int]]):
        self._tokens = tokens
        self._stack = []
        self._list = []

    def calc(self):
        for token in self._tokens:
            if isinstance(token, int):
                self._list.append(token)
            elif token == "(":
                self._stack.append(token)
            elif token == ")":
                while (op := self._stack.pop()) != "(":
                    y = self._list.pop()
                    x = self._list.pop()
                    func = self.map[op]
                    result = func(x, y)
                    self._list.append(result)
            else:
                priority1 = self.priority[token]
                if self._stack:
                    op = self._stack[-1]
                    if op != "(":
                        priority2 = self.priority[self._stack[-1]]
                        while priority1 < priority2:
                            op = self._stack.pop()
                            y = self._list.pop()
                            x = self._list.pop()
                            func = self._map[op]
                            result = func(x, y)
                            self._list.append(result)
                            if self._stack:
                                priority2 = self.priority[self._stack[-1]]
                            else:
                                priority2 = -1
                self._stack.append(token)

        while self._stack:
            op = self._stack.pop()
            y = self._list.pop()
            x = self._list.pop()
            func = self.map[op]
            result = func(x, y)
            self._list.append(result)

        return self._list[0]


if __name__ == "__main__":
    tokens = modify(read())
    print(tokens)
    calculator = Calculator(list(tokens))
    print(calculator.calc())
