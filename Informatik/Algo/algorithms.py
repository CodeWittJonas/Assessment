import random


def bubbleSort(list_to_sort):
    for i in range(len(list_to_sort) - 1, 0, -1):
        for j in range(len(list_to_sort) - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                swap(list_to_sort, j, j + 1)


# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selectionSort(arr):
    for i in range(len(arr) - 1):

        min = i

        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        swap(arr, min, i)


def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]

    while i < j:
        while arr[i] <= pivot and i < j:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            swap(arr, i, j)
    arr[low] = arr[j]
    arr[j] = pivot
    return j


def quicksort(arr, left, right):
    middle = partition(arr, left, right)
    quicksort(arr, left, middle - 1)
    quicksort(arr, middle + 1, right)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def towersOfHanoi(n, start, end, helper):
    if n == 1:
        print("Move 1 from {} to {}.".format(start, end))
        return
    towersOfHanoi(n - 1, start, helper, end)
    print("Move {} from {} to {}.".format(n, start, end))
    towersOfHanoi(n - 1, helper, end, start)


def searchmissing(arr, size):
    a = 0
    b = size - 1
    mid = 0
    while b > a + 1:
        mid = (a + b) // 2
        if (arr[a] - a) != (arr[mid] - mid):
            b = mid
        elif (arr[b] - b) != (arr[mid] - mid):
            a = mid
    return arr[mid] + 1


def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


def find_floor(arr, l, r, key):
    mid = (l + r) // 2

    if r - l <= 1:
        if key < arr[r]:
            return arr[l]
        elif key == arr[r]:
            return arr[r]
        else:
            return -1
    elif key >= arr[mid]:
        find_floor(arr, mid, r, key)
    elif key < arr[mid]:
        find_floor(arr, l, mid, key)
    else:
        return -1


# ==============================================================================================================


if __name__ == '__main__':
    arr = [2, 9, 5, 7, 94, 3, 1, 42, 11, -1, 4, 12, 8, 10]

    print(quicksort(arr, 0, len(arr) - 1))
