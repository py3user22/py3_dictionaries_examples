#!/bin/python3


"""
Work with else
You know that when you use an if statement, the body of the program will run only if the test expression is True.
 o add more code that will run when your test expression is False, you need to add an else statement.
"""

a = 27
b = 93
if a <= b:
    print("{} is less than or equal to b".format(a))
elif a == b:
    print("a is equal to be")
else:
    print(b)

print("\n----------------\n")

c = 27
d = 93

if c < d:
    print("c is less than d")
elif c > b:
    print("c is greater than d")
else:
    print("c is equal to d")

print("\n----------------\n")

"""Work with nested conditional logic
Python also supports nested conditional logic,
meaning that you can nest if, elif, and else statements to create even more complex programs.
to nest conditions, indent the inner conditions, and everything at the same level of indentation
will be run in the same code block: """

aa = 16
bb = 25
cc = 27

if aa > bb:
    if bb > cc:
        print("aa > bb, & bb  > cc")
    else:
        print("aa > bb, & aa < cc")
elif aa == bb:
    print("aa is equal to bb")
else:
    print("aa < bb")

print("\n----------------\n")

