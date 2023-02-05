#!/usr/bin/python3


# C:\Users\jesus\AppData\Roaming\JetBrains\PyCharmCE2022.3\scratches\204_dictionary52.py

# create a dictionary
dictionary = {}                 # curly braces method
another_dictionary = dict()     # dict method

print(type(dictionary))                     # <class 'dict'>
print(type(another_dictionary))             # <class 'dict'>
print(dictionary == another_dictionary)     # >> True
print("--------------------------\n")

# populate the dictionary
dictionary["key1"] = "value1"

# access key1
print(dictionary["key1"])                   # value1


# create a dictionary w/ preinserted keys/values
dictionary = {"key1": "value1"}
print(dictionary["key1"])                   # value1
print("--------------------------\n")

# keyword argument list
dictionary = dict(key1="value1", key2="value2")

# display the dictionary
print(dictionary)                           # {'key1': 'value1', 'key2': 'value2'}


# list of tuples
dictionary = dict([("key1", "value1"), ("key2", "value2")])

# display the dictionary
print(dictionary)                           # {'key1': 'value1', 'key2': 'value2'}
print("--------------------------\n")


# Add more elements to the dictionary
dictionary[42] = "the answer to the ultimate question of life, the universe, and everything."
dictionary[1.2] = ["one point two"]
dictionary["list"] = ["just", "a", "list", "with", "an", "integer", 3]

# Display the dictionary
print(dictionary)


# Modify a value
dictionary["list"] = ["it's another", "list"]

# Display the dictionary
print(dictionary)
print()


print("--------------------------\n")
# Access the value of "list"
print(dictionary["list"])                           # ["it's another", 'list']




# Dictionary with duplicate keys, try to create a dictionary w/ duplicate keys
duplicated_keys = {"key1": "value1", "key1": "value2", "key1": "value3"}

# Access key1 will print the
print(duplicated_keys["key1"])                      # value3

print("--------------------------\n")





