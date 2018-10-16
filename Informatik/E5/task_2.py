import csv
import os
import operator


def read_csv(filename):
    """
    This function reads a csv file and returns a list with all rows. We use it to receive a list containing all the
    rows and to avoid having to read the file multiple times in the different functions. Having a list to work with is
    convenient, as we can iterate over it and perform other operations very easily.

    :param filename: A string containing the name of the csv file to read
    :return: A list of OrderedDict files with all rows of the csv file
    """
    if not os.path.isfile(filename):
        print('ERROR: "{0}" file not found'.format(filename))
        exit()

    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        lines = []
        for row in reader:
            lines.append(row)

        return lines


def preview_dognames(list, n):
    """
    Returns a preview of the dog names of the top n rows in the list (no filtering, i.e. double entries are allowed)

    Example: If the top of the csv looked like this:

    HUNDENAME       GEBURTSJAHR_HUND    GESCHLECHT_HUND
    Adam            2000                m
    Berta           2001                w
    Collin          2006                m
    Collin          2007                m
    Eve             2008                w

    A call 'preview_dognames(list, 4)' should return the list ['Adam', 'Berta', 'Collin', 'Collin']

    :param list: The list created from the csv file
    :param n: The number of lines to return the dog name
    :return: A list of strings, containing n entries of dog names
    """

    pass


def dognames_count(list):
    """
    Returns a dictionary containing entries with each unique dog name and the number of occurences in the list.
    The order in the dictionary does not matter, i.e. it does not have to be an OrderedDict.

    Example: If the top of the csv looked like this:

    HUNDENAME       GEBURTSJAHR_HUND    GESCHLECHT_HUND
    Adam            2000                m
    Berta           2001                w
    Collin          2006                m
    Collin          2007                m
    Eve             2008                w

    A call 'dognames_count(list)' should return the dictionary
    { 'Adam': 1, 'Berta': 1, 'Collin': 2, 'Eve': 1 }


    :param list: The list created from the csv file
    :return: A dictionary containing one key-value pair for each unique dog name, with the dog name (string) as
    key and the number of occurrences of that name (int) as value
    """

    pass


def top_n_dognames(list, n):
    """
    Returns a sorted list with tuples (dogname, count) with the top n most used dog names, starting with the highest one

    Example: If the top of the csv looked like this:

    HUNDENAME       GEBURTSJAHR_HUND    GESCHLECHT_HUND
    Adam            2000                m
    Berta           2001                w
    Collin          2006                m
    Collin          2007                m
    Eve             2008                w

    A call 'top_n_dognames(list, 1)' should return this list with one entry: [('Collin', 2)]

    :param list: The list created from the csv file
    :param n: The number of entries that should be returned
    :return: A sorted list with tuples (dogname, count) with the top n most used dog names, starting with the highest one
    """

    pass


def is_valid_row(row, year=None, sex=None):
    """
    A helper function that returns True if a row satisfies the specified filter constraints, False otherwise.
    The row should be of type OrderedDict, so you can use the entries of the list that you create in read_csv
    directly, without modifying it.

    Example:

    row = OrderedDict([('HUNDENAME', 'Adam'), ('GEBURTSJAHR_HUND', '2006'), ('GESCHLECHT_HUND', 'm')])

    is_valid_row(row) --> no filter specified, this should always return True
    is_valid_row(row, sex='w') --> should return False (wrong sex)
    is_valid_row(row, year=1994, sex='m') --> should return False (wrong year)
    is_valid_row(row, year=2006, sex='m') --> should return True

    :param row: An entry of the list created from the csv file, with data type OrderedDict
    :param year: An integer parameter specifying the birth year. Any integer is accepted, or None if no filter should be applied.
    :param sex: A string parameter specifying the sex. Possible values: 'm', 'w' or None if no filter should be applied.
    :return: True if a row satisfies the specified filter constraints, False otherwise.
    """

    return True


def filter_dognames(list, year=None, sex=None):
    """
    Returns a filtered list with entries of type OrderedDict, containing all entries from the given list where the given
    parameters apply. Note that you don't have to change the type of the rows that you get from the list, you only need
    to filter out the ones that don't satisfy the filter conditions.

    It is strongly recommended, but not mandatory to use the previously defined helper function is_valid_row to filter
    the list. If you use this helper function, this one will be a short and simple function.

    Example: If the top of the csv looked like this:

    HUNDENAME       GEBURTSJAHR_HUND    GESCHLECHT_HUND
    Adam            2006                m
    Berta           2009                w
    Collin          2006                m
    Collin          2007                m
    Eve             2006                w

    A call 'filter_dognames(list, year=2006, sex='m')' should return this list:
    [
        OrderedDict([('HUNDENAME', 'Adam'), ('GEBURTSJAHR_HUND', '2006'), ('GESCHLECHT_HUND', 'm')]),
        OrderedDict([('HUNDENAME', 'Collin'), ('GEBURTSJAHR_HUND', '2006'), ('GESCHLECHT_HUND', 'm')])
    ]

    :param list: The list created from the csv file
    :param year: An integer parameter specifying the birth year. Any integer is accepted, or None if no filter should be applied.
    :param sex: A string parameter specifying the sex. Possible values: 'm', 'w' or None if no filter should be applied.
    :return:
    """

    pass


if __name__ == '__main__':
    """
    Read in the data from a csv file and perform some data science on it.
    """
    filename = './dognames.csv'

    # Read the file and store it in a list with OrderedDict entries, each one containing the contents of one line.
    # This function has already been implemented for you.
    dognames = read_csv(filename)

    # Print a preview of the list, containing the first n dog names
    print(preview_dognames(dognames, 5))

    # Print the number of occurrences of each unique dog name in the list
    print(dognames_count(dognames))

    # Print the top n most used dog names and their counts
    print(top_n_dognames(dognames, 5))

    # Filter the list to get only dogs for a specific year and/or sex
    print(filter_dognames(dognames, 1998, 'm'))
