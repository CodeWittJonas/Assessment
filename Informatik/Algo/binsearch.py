def binsearch(array, number):
    left = 1
    right = len(array) + 1
    middle = (right + left)//2

    while left <= right and number != array[middle]:
        if number < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
        middle = (left + right)//2

    if left <= right:
        return middle
    else:
        return None


if __name__ == '__main__':

    array = []
    for i in range(1000):
        array.append(i)

    print(binsearch(array, 34))
