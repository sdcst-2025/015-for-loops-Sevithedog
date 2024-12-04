#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""
try:
    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
except:
    print("Invalid input")
    exit()
if width > 10:
    print('invalid input')
    exit()

row = height
stars = width

for row in range(1,(height+1)):
    for stars in range(1,width):
        print("*", end = "")
    print("*")
    
