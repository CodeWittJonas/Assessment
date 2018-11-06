def list_duplicates(sequence):
    """
    Takes as input a list of numbers and returns a list of tuples,
    where each tuple contains, the value of the duplicate and the indexes at which the value occurs.

    E.g. list_duplicates([1, 2, 1, 2, 3, 4, 5, 6, 7, 4]) == [(1, (0, 2)), (2, (1, 3)), (4, (5, 9))]

    :param sequence: A list of numbers
    :return: List of tuples of duplicates and their indexes.
    """
    if not sequence:
        return sequence

    occurrences = {}
    for idx, element in enumerate(sequence):
        if element in occurrences:
            occurrences[element].append(idx)
        else:
            occurrences[element] = [idx]

    return [(element, tuple(occurrences[element])) for element in occurrences if len(occurrences[element]) > 1]


if __name__ == '__main__':

    print(list_duplicates([1, 2, 1, 2, 1]))

    print(list_duplicates([4.0, 4, 4.0, 4]))
