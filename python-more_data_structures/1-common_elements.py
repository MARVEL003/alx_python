def common_elements(set_1, set_2):
    common_set = set()

    for element in set_1:
        if element in set_2:
            common_set.add(element)

    return common_set


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_elements_set = common_elements(set1, set2)