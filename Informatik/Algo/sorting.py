def bubbleSort(list_to_sort):

    for j in range(len(list_to_sort)):
        for i in range(len(list_to_sort)-1):
            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]

    return list_to_sort


def insertionSort(list_to_sort):

    for i in range(len(list_to_sort)):

        for j in range(i+1):
            pass

# ==============================================================================================================


if __name__ == '__main__':
    unorderered = [4, 8, 29, 3, 6, 9]

    print(bubbleSort(unorderered))

