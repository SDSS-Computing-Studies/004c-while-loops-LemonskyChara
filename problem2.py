#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""

a = int(input("Enter a integer "))
b = a * 12
a1 = int(a)
count = 0
while a1 != b:
    count = count + 1
    a1 = a * count
    print(a1 ,end=" ")
