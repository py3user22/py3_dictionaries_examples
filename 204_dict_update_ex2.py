#!/usr/bin/python3


"""The update() method is useful whenever we want to merge dictionaries or add new key:value pairs using an iterable
(iterables are, for instance, lists or tuples)."""


# Create a Harry Potter dictionary
harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor"
}

# Display the dictionary
print(harry_potter_dict)
# >>  {'Harry Potter': 'Gryffindor', 'Ron Weasley': 'Gryffindor', 'Hermione Granger': 'Gryffindor'}


"""Let’s now add other characters and their houses using different options we have available for the update() method:"""
# Characters to add to the Harry Potter dictionary
add_characters_1 = {
    "Albus Dumbledore": "Gryffindor",
    "Luna Lovegood": "Ravenclaw"
}

# Merge dictionaries
harry_potter_dict.update(add_characters_1)

# Display the dictionary
print(harry_potter_dict)
# >> {'Harry Potter': 'Gryffindor', 'Ron Weasley': 'Gryffindor', 'Hermione Granger': 'Gryffindor',
# >> 'Albus Dumbledore': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw'}


"""We can also use an iterable to add new elements to the dictionary:"""
# Use iterables to update a dictionary
add_characters_2 = [
    ["Draco Malfoy", "Slytherin"],
    ["Cedric Diggory", "Hufflepuff"]
]
harry_potter_dict.update(add_characters_2)

print(harry_potter_dict)
# >> {'Harry Potter': 'Gryffindor', 'Ron Weasley': 'Gryffindor', 'Hermione Granger': 'Gryffindor',
# >> 'Albus Dumbledore': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw',
# >> 'Draco Malfoy': 'Slytherin', 'Cedric Diggory': 'Hufflepuff'}


"""We used a list of lists where the first element of each list is the character name and the second
element is their house. The update() method then will automatically associate the first element (key)
with the second element (value). For the sake of the experiment, try to update the dictionary with a
 ist of lists but with three elements in each nested list."""

# Use iterables to update a dictionary
add_characters_3 = [
    ("Rubeus Hagrid", "Gryffindor"),
    ("Minerva McGonagall", "Gryffindor")
]
harry_potter_dict.update(add_characters_3)

print(harry_potter_dict)

# >> {'Harry Potter': 'Gryffindor', 'Ron Weasley': 'Gryffindor', 'Hermione Granger': 'Gryffindor',
# >> 'Albus Dumbledore': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw',
# >> 'Draco Malfoy': 'Slytherin', 'Cedric Diggory': 'Hufflepuff',
# >> 'Rubeus Hagrid': 'Gryffindor', 'Minerva McGonagall': 'Gryffindor'}


