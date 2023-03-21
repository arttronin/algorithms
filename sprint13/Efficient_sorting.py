# 84343414

class Participant:
    def __init__(self, login, resolved, sanction):
        self.login = login
        self.resolved = -int(resolved)
        self.sanction = int(sanction)

    def __lt__(self, other):
        if isinstance(other, Participant):
            return (
                (self.resolved, self.sanction, self.login) <
                (other.resolved, other.sanction, other.login)
            )

    def __str__(self):
        return self.login


def effective_fast_sort(array, left, right):
    if left >= right:
        return

    prev_left = left
    prev_right = right
    pivot = array[(left + right) // 2]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    effective_fast_sort(array, left, prev_right)
    effective_fast_sort(array, prev_left, right)


if __name__ == "__main__":
    array_lenght = int(input())
    array = []
    for items in range(array_lenght):
        array.append(Participant(*input().split()))
    effective_fast_sort(array, 0, len(array) - 1)
    print(*array, sep="\n")
