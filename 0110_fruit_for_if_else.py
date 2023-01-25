#!/bin/python3


fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']


"""
iterate thru the dictionary
"""
for object, cnt in basket_items.items():
    if object in fruits:
        fruit_count += cnt
    else:
        not_fruit_count += cnt

print("Number of fruits = {}\nNon-fruit objects = {}".format(fruit_count, not_fruit_count))

# >> Number of fruits = 23
# >> Non-fruit objects = 11
