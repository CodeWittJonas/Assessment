def stringify(n):
    if not isinstance(n, int) or not isinstance(n, float):
        raise ValueError("please enter number")
    if n % 2 == 0:
        return "{} is even".format(n)
    else:
        return "{} is odd".format(n)


def compute_stats(lst):
    if not isinstance(lst, ):
        raise ValueError

    second_highest, average, median = 0, 0, 0
    for number in lst:
        if isinstance(number, int):
            average += number
        else:
            raise ValueError
    average = average / len(lst)
    second_highest = lst
    second_highest.remove(max(second_highest))
    second_highest = max(second_highest)

    if len(lst) % 2 == 0:
        for i in range(int(len(lst)/2-1)):
            lst.remove((max(lst)))
            lst.remove(min(lst))
        median = (max(lst) + min(lst))/2
    else:
        for i in range(int((len(lst)-1)/2)):
            lst.remove(max(lst))
            lst.remove(min(lst))
        median = lst[0]
    return [second_highest, average, median]


def count_letters(s):
    if not isinstance(s, str):
        raise ValueError

    letters = {"upper": 0, "lower": 0}
    for letter in s:
        if letter.isupper():
            letters["upper"] += 1
        elif letter.islower():
            letters["lower"] += 1
        else:
            pass
    return letters


class Shape(object):

    def __init__(self):
        pass

    def description(self):
        return "{} with area {}".format(type(self).__name__, self.area())

    def area(self):
        return 0


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def description(self):
        return super().description()

    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def description(self):
        return super().description()

    def area(self):
        return 3 * self.radius**2


class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width, width)

    def area(self):
        return super().area()

    def description(self):
        return super().description()


def e():
    for i in {'a': 1, 'b': 2, 'c': 3}:
        return i


def insert_into_list(l, pos, *args):
    for a in args:
        l.insert(pos, a)
    return l


class g(object):
    x = 1.2

    def __init__(self):
        self.x = 3

def fun(n):
    if n <= 100:
        return fun(fun(n+11))
    else:
        return n - 10


# ======================================================================================================================


if __name__ == '__main__':

    print(fun(89))

