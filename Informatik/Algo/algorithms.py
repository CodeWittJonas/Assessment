def bubbleSort(list_to_sort):
    for j in range(len(list_to_sort)):
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]

    return list_to_sort


def insertionSort(list_to_sort):
    for i in range(len(list_to_sort)):

        for j in range(i + 1):
            pass


def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# ==============================================================================================================


if __name__ == '__main__':

    for i in range(10):
        print(fib(i))
