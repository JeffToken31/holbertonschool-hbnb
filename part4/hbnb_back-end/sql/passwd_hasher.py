#!/usr/bin/python3
import bcrypt

password = b"admin1234" # "b" before "admin1234" is same as password.encode()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())
password2 = b"user1234"
hashed2 = bcrypt.hashpw(password2, bcrypt.gensalt())
print(hashed2.decode())
