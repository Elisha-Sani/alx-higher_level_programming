#!/usr/bin/python3
def uppercase(str):
    print("".join("{}".format(chr(ord(char) - 32))
        if 97 <= ord(char) <= 122
        else "{}".format(char) for char in str), end="")
    print()
