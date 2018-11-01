def find_max(lst):
    max_value = 0
    last_num = 0
    for number in lst:
        if number > max_value and number > last_num:
            max_value = number
        last_num = number

    return max_value


def e():
    for i in {'a': 1, 'b': 2, 'c': 3}:
        print(i)


def sum(a, b):
    if b is None:
        return a + 1
    else:
        return a + b


def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True


def find_last(line, ch):

    length = len(line) - 1

    if ch not in line:
        return -1
    if line is None:
        return -1

    if line[length] == ch:
        return length
    else:
        line = line[:-1]
        return find_last(line, ch)


def build_words_dict(filename, min_occurences):
    content = ""
    output_dict = {"UNK": 0}
    with open(filename, 'r') as file:
        for line in file.readlines():
            content = content + line
        file.close()

    list_of_words = content.split()

    for word in list_of_words:
        occurences = 0
        for i in range(len(list_of_words)):
            if list_of_words[i] == word:
                occurences += 1
        if occurences >= min_occurences:
            output_dict[word] = occurences
        else:
            output_dict['UNK'] += 1

    return output_dict


def factorial_recursive(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursive(number - 1)


def weighted_sum_recursive(numbers, depth=1):
    result = 0

    for number in numbers:
        if isinstance(number, int):
            result += depth * number
        elif isinstance(number, list):
            result += weighted_sum_recursive(number, depth+1)

    return result


# ======================================================================================================================

if __name__ == '__main__':

    numbers = [1,2,3, [1, 2, [3]]]

    print(weighted_sum_recursive(numbers))
