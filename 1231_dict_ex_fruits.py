#!/usr/bin/python3


result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

"""Count the number of fruits in basket,
     count only fruits that match fruits list"""

for key, value in basket_items.items():
    if key in fruits:
        result += value

print(result)      # >> 23
