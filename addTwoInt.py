#!/bin/python3

import sys

print(sys.argv)

a = int( sys.argv[1] )
b = int( sys.argv[2] )


def add(a,b):
    x = a + b
    print(x)

try:
    a = int( sys.argv[1] )
    b = int( sys.argv[2] )

except IndexError:
    print ("Error. 2 numerical valors")
    a = int(input("Entrez la premiere valeur : "))
    b = int(input("Entrez la dexieme valeur : "))
    add(a,b)
    raise (SystemExit)

add(a,b)


