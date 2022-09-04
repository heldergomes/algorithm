def reach_kaprekar_constant(param, interation):
    """
    It's necessary convert the integer in a list of string, because the function
    sorted() only knows how to sort ARRAYS, therefore if it's necessary sort an
    integer number, must have to convert the integer in a string array, sort the
    array and also convert again the string array in integer.
    """
    integer_decoded = [x for x in str(param)]  # O(n)
    asc_param = int("".join(sorted(integer_decoded)))  # O(n log n)
    desc_param = int("".join(sorted(integer_decoded, reverse=True)))  # O(n log n)

    result = desc_param - asc_param
    print(f'{desc_param} - {asc_param} = {result}')

    if result == 6174:
        return interation
    return reach_kaprekar_constant(param=result, interation=interation+1)


if __name__ == '__main__':
    print(reach_kaprekar_constant(9876, 1))
