#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""

name = ""
password = ""
while name != "admin":
    name = input("username: ").strip()
    if name != "admin":
        print("Access denied")
while password != "12345":
    password = input("password: ").strip()
    if password != "12345":
        print("Access denied")
print("Access granted")
