Python provides various data structures to work with collections of data. In this task, I'll cover sets and dictionaries, which are commonly used data structures for different purposes.

Sets.
- A set is an unordered collection of unique elements. In Python, sets are defined using curly braces {} or the set() constructor. Here's how you can work with sets in Python:

# Creating a set
my_set = {1, 2, 3, 4}

# Adding elements to a set
my_set.add(5)

# Removing elements from a set
my_set.remove(2)

# Checking if an element is in a set
if 3 in my_set:
    print("3 is in the set")

# Iterating over a set
for item in my_set:
    print(item)

Dictionaries.
- A dictionary is a collection of key-value pairs, where each key is unique. In Python, dictionaries are defined using curly braces {} or the dict() constructor. Here's how you can work with dictionaries in Python:

# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values by key
print(my_dict['name'])  # Output: 'John'

# Adding new key-value pairs
my_dict['job'] = 'Engineer'

# Modifying values
my_dict['age'] = 31

# Removing key-value pairs
del my_dict['city']

# Checking if a key is in a dictionary
if 'job' in my_dict:
    print("Job:", my_dict['job'])

# Iterating over a dictionary
for key, value in my_dict.items():
    print(key, ":", value)
    
Sets are useful when you need to store a collection of unique items, while dictionaries are handy for storing and retrieving key-value pairs. Both data structures are versatile and commonly used in Python programming for various tasks.




