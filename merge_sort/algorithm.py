def merge(left_list, right_list):
    sorted_list = []
    size_bigger_list = len(left_list) + len(right_list)

    for _ in range(size_bigger_list):
        if len(left_list) == 0:
            sorted_list.append(right_list.pop(0))
        elif len(right_list) == 0:
            sorted_list.append(left_list.pop(0))
        else:
            if left_list[0] > right_list[0]:
                sorted_list.append(right_list.pop(0))
            else:
                sorted_list.append(left_list.pop(0))
    return sorted_list


def merge_algorithm(unsorted_list):
    unsorted_list_size = len(unsorted_list)
    if unsorted_list_size == 1:
        return unsorted_list

    left_side = unsorted_list[0:unsorted_list_size//2]
    right_side = unsorted_list[-unsorted_list_size//2:]

    left_list = merge_algorithm(left_side)
    right_list = merge_algorithm(right_side)
    
    return merge(left_list, right_list)


if __name__ == '__main__':
    unsorted_list = [12, 77, 13, 5, 6, 44, 44, 6, 34, 1, 22]
    print(merge_algorithm(unsorted_list))