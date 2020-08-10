def find_max(array):
    max_ = array[0]
    for number in array:
        if number > max_:
            max_ = number
    return max_