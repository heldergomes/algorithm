import random


def binary_search(list, target, low, high):
    if low <= high:
        middle = (low + high) // 2
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            return binary_search(
                list=list,
                target=target,
                low=middle + 1,
                high=high
            )
        else:
            return binary_search(
                list=list,
                target=target,
                low=low,
                high=middle - 1
            )
    return False


if __name__ == '__main__':
    # Creation of randomic and sorted items
    listf = [random.randint(1, 10000) for _ in range(10000)]
    listf = sorted(list(set(listf)))
    # Variables to control the movements into the array
    low = 0
    high = len(listf) - 1
    target = 5

    result = binary_search(
        list=listf,
        target=target,
        low=low,
        high=high
    )
    if result:
        print(f'The index of the query {target} is {result}')
    else:
        print(f'The query {target} was not found')
