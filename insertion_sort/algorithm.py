def sort_algorithm(unsorted_list):
    for index in range(len(unsorted_list)):
        key = index + 1
        while len(unsorted_list) > key > 0 and unsorted_list[key - 1] > unsorted_list[key]:
            previous_integer = unsorted_list[key - 1]
            unsorted_list[key - 1] = unsorted_list[key]
            unsorted_list[key] = previous_integer
            key -= 1
    return unsorted_list


"""
    This algorithm run the same logic than the algorithm above,
    however this algorithm use less instructions to do the same thing
"""


def sort_algorithm_compressed(unsorted_list):
    for index in range(1, len(unsorted_list)):
        key_data = unsorted_list[index]
        prev_index = index - 1
        while prev_index >= 0 and key_data < unsorted_list[prev_index]:
            unsorted_list[prev_index + 1] = unsorted_list[prev_index]
            prev_index -= 1
        unsorted_list[prev_index + 1] = key_data
    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [12, 11, 13, 5, 6, 44, 44, 6, 34, 1, 22]
    print(sort_algorithm(unsorted_list))
