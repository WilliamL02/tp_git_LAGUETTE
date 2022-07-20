#!/bin/python3

import sys

print(sys.argv)


def add(a,b):
    x = a + b
    print(x)

a = int( sys.argv[1] )
b = int( sys.argv[2] )

add(a,b)