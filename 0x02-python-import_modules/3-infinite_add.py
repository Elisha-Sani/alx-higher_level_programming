#!/usr/bin/python3
import sys

if __name__ == "__main__":
    #convert arguments to integers and calc
    sum_args = sum(int(arg) for arg in sys.argv[1:])
    print(sum_args)
