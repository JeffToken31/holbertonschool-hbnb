#!/usr/bin/python3
from sys import argv
import uuid
"""
Print numbers of desired uuid else print one
"""


if len(argv) == 1:
    print(str(uuid.uuid4()))
    exit()
if int(argv[1]) > 1:
    for i in range(int(argv[1])):
        print(str(uuid.uuid4()))
else:
    print(str(uuid.uuid4()))
