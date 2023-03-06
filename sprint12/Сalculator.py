# 83531100
# использую модель operator, почитал так же про lambda-функцию.
# На мой взгляд, модуль оператор в коде смотрится более читаемым и понятным

import operator

OPERATIONS = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
    '/': operator.floordiv
}


class Stack:
    """Стек для хранения чисел."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляем новый элемент."""
        self.items.append(item)

    def pop(self):
        """Удаляем и возвращаем последний элемент."""
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('В хранилище отсутствуют элементы')


def calculator(symbols):
    stack = Stack()
    for symbol in symbols:
        try:
            stack.push(int(symbol))
        except ValueError:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.push(OPERATIONS[symbol](operand_2, operand_1))
    return stack.pop()


if __name__ == '__main__':
    print(calculator(input().split()))
