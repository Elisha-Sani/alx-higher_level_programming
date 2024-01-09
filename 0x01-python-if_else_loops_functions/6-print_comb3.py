#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i+1, 10):
        print("{:d}{:d}, ".format(i, j), end="")
print("{:d}{:d}, ".format(7, 9), end="")
print("{:d}{:d}".format(8, 9))
