#!/bin/python3


""" Exercise: Use logic to examine an object's size
You will start your project by creating the code to determine if a piece of space debris is of a dangerous size.
For this exercise we will use an arbitrary
size of 5 meters cubed (5m3);
anything larger is a potentially dangerous object.

For this step you will be presented with the goal for the exercise, followed by an empty cell.
Enter your Python into the cell and run it. The solution is at the bottom of the exercise.

In the cell below, add a variable named object_size and set it to 10 to represent 10m3.
then add an if statement to test if object_size is greater than 5.
if it is, display a message saying We need to keep an eye on this object.
If it's less than 5, display a message saying Object poses no threat.
"""

object_size = 10
proximity = 9000
if object_size > 5 and proximity < 1000:
    print("We need to keep an eye out on this object\n"
          "Evasive maneuvers required")
else:
    print("Object poses no threat")

print("\n-----------------------\n")

"""Exercise: Use complex logic to determine possible evasive maneuvers
In the previous exercise you created code to test the size of the object.
Now you will test both the object's size and proximity. You will use the same threshold for size of 5m3.
If the object is both larger than the threshold and within 1000km of the ship evasive maneuvers will be required.

For this step you will be presented with the goal for the exercise, followed by an empty cell.
Enter your Python into the cell and run it. The solution is at the bottom of the exercise.

Add the code to the cell below to create two variables: object_size and proximity.
Set object_size to 10 to represent 10m3. Set proximity to 9000.

Then add the code to display a message saying Evasive maneuvers required if both object_size is greater than 5,
and proximity is less than 1000. Otherwise display a message saying Object poses no threat.
"""




print("\n-----------------------\n")
# or operator

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

print("\n-----------------------\n")

fact = "The Moon has no atmosphere. "
two_facts = fact + "No sound can be heard on the Moon."
moon_radius = "The Moon has a radius of 1,080 miles."
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
heading = "temperatures and facts about the moon"
heading_upper = heading.title()
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures .split('\n')


print(heading_upper)
print(multiline)
print(two_facts)
print(temperatures_list)

print("-----------------------\n")




