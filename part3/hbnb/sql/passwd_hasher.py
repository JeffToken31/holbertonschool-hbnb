#!/usr/bin/python3
import bcrypt

password = b"admin1234" # "b" before "admin1234" is same as password.encode()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())
password2 = "user1234"
password2.encode()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())
