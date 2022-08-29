"""
    This algorithm can calculate 2 to the power N value without use multiplication,
    only using recursive functions
"""


def recursive_exponential_equation(value):
    if value <= 0:
        return 1
    return recursive_exponential_equation(value - 1) + recursive_exponential_equation(value - 1)


if __name__ == '__main__':
    print(recursive_exponential_equation(5))
