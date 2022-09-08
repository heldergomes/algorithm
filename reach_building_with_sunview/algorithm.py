"""
Basically, the idea was to read the array from the end to the beginning and save the latest
big building found, so that way was able to develop the algorithm with O(n)
"""


def reach_building_with_sunview(param):
    index = len(param) - 1
    biggest_building = -1
    sun_view_counter = 0

    for _ in range(len(param)):
        if param[index] > biggest_building:
            biggest_building = param[index]
            sun_view_counter += 1
        index -= 1

    return sun_view_counter


if __name__ == '__main__':
    building_list = [15, 14, 8, 13, 6, 9]
    print(reach_building_with_sunview(building_list))
