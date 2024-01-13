#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    operations = [("+", add(a, b)), ("-", sub(a, b)), ("*", mul(a, b)), ("/", div(a, b))]
    for op, result in operations:
        print(f"{a} {op} {b} = {result}")
