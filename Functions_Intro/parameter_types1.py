def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:....{}, {}"
          .format(p1, p2))
    print("var-positional (*args):...{}".format(args))
    print("Keyword:..................{}".format(k))
    print("var-keyword:..............{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)


def sum_numbers(*values: float) -> float:
    """
    Calculates the sum of a tuple
    :param values: the tuple of values
    :return: return the sum of the values from the tuple
    """
    sum = 0
    for i in values:
        sum += i

    return sum


print(sum_numbers(1, 2, 3))
print(sum_numbers(4, 5, 6))
print(sum_numbers(7, 8, 9))
print(sum_numbers(10, 11, 12))
print(sum_numbers(13, 14, 15))
print(sum_numbers(16, 17, 18))

