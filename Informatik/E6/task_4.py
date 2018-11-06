def swap_case(s=None):
    """
    Swaps the case of a String changing upper case to lower case,
    and lower case to upper case.
          * swap_case("The dog has a BONE") = "tHE DOG HAS A bone"

    :param s: the string to swap case, may be None
    :return: the changed String, None if None input
    """
    if s:
        return s.swapcase()
    else:
        return s


if __name__ == '__main__':

    print(swap_case())
