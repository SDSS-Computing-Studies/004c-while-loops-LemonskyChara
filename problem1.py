##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Acces denied
"""

name = ""
password = ""
count = 0
count1 = 0
while name != "admin":
    name = input("username: ").strip()
    if name != "admin":
        print("Access denied")
    count = count + 1
    if count == 3:
        exit()
while password != "12345":
    password = input("password: ").strip()
    if password != "12345":
        print("Access denied")
    count1 = count1 + 1
    if count1 == 3:
        exit()
print("Access granted")
