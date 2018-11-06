def quick_sort(array):
    """
    Takes as input a list of numbers, sorts it in ascending order and returns the sorted list.

    :param array: A list of numbers
    :return: The same list, sorted in ascending order
    """

    if not array:
        return array

    less = []
    equal = []
    greater = []

    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
        if x == pivot:
            equal.append(x)
        if x > pivot:
            greater.append(x)

    return quick_sort(less) + equal + quick_sort(greater)

if __name__ == '__main__':

    print(quick_sort())
