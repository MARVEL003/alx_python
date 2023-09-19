def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


my_dict = {'name': 'John', 'age': 30}

updated_dict = update_dictionary(my_dict, 'age', 31)

updated_dict = update_dictionary(my_dict, 'city', 'Canada')