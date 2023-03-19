# 84245842

class Participant:
    def __init__(self, login, resolved, sanction):
        self.login = login
        self.resolved = -int(resolved)
        self.sanction = int(sanction)

    def __gt__(self, other):
        if self.resolved != other.resolved:
            return self.resolved > other.resolved
        if self.sanction != other.sanction:
            return self.sanction > other.sanction
        return self.login > other.login

    def __str__(self):
        return self.login


def effective_fast_sort(array, left, right):
    if left >= right:
        return

    counter = left
    for element in range(left, right):
        if array[right] > array[element]:
            array[counter], array[element] = array[element], array[counter]
            counter += 1
    array[counter], array[right] = array[right], array[counter]

    effective_fast_sort(array, left, counter - 1)
    effective_fast_sort(array, counter + 1, right)


if __name__ == "__main__":
    array_lenght = int(input())
    array = []
    for items in range(array_lenght):
        array.append(Participant(*input().split()))
    effective_fast_sort(array, 0, len(array) - 1)
    print(*array, sep="\n")
