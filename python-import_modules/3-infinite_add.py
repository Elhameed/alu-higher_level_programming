#!/usr/bin/python3

import sys

if __name__ == '__main__':
    args = sys.argv[1:]

    # Convert each argument to an integer and sum them up
    total = sum(int(arg) for arg in args)

    # Print the total
    print(total)
