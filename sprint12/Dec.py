# 83353773
class Dec:

    def __init__(self, max_size):
        # кольцевой буфер
        self.elements = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = -1
        self.size = 0

    def push_back(self, value):
        # добавляем элемент в конец дека
        if self.size == self.max_size:
            raise IndexError('Максимальное число элементов')
        self.tail = (self.tail + 1) % self.max_size
        self.elements[self.tail] = value
        self.size += 1

    def push_front(self, value):
        # добавляем элемент в начало дека
        if self.size == self.max_size:
            raise IndexError('Максимальное число элементов')
        self.head = (self.head - 1) % self.max_size
        self.elements[self.head] = value
        self.size += 1

    def pop_front(self):
        # выводим первый элемент дека и удаляем его
        if self.size == 0:
            raise IndexError('Дек элементов пуст')
        front = self.elements[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return front

    def pop_back(self):
        # выводим последний элемент дека и удаляем его
        if self.size == 0:
            raise IndexError('Дек элементов пуст')
        back = self.elements[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return back


if __name__ == '__main__':
    count_command = int(input())
    deque = Dec(int(input()))
    for _ in range(count_command):
        action, *values = input().split()
        try:
            result = getattr(deque, action)(*values)
            if result is not None:
                print(result)
        except IndexError:
            print('error')
        except AttributeError:
            raise AttributeError(f'Некорректный атрибут {action} для {deque}')

# теория к концу все хуже и хуже, спасибо youtube за помощь)
