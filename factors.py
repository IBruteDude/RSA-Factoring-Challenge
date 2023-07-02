#!/usr/bin/python3
from sys import argv, exit, stderr
from math import ceil, sqrt

class FactorisationError(Exception):
    pass

def exhaustive_factorisation(N):
    n = 3
    while N % n != 0:
        n += 2
        if n > 1000000:
            raise TimeoutError
    return (N // n, n)

def fermat_factorisation(N):
    if N % 2 == 0:
        return  (N // 2, 2)
    try:
        a, b = exhaustive_factorisation(N)
        return (a, b)
    except TimeoutError:
        pass
    a = ceil(sqrt(N))
    b2 =  a*a - N
    while int(sqrt(b2)) != sqrt(b2):
        a = a + 1
        b2 = a*a - N
    return (int(a + sqrt(b2)), int(a - sqrt(b2)))

if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: ./factors filename [filename]*", file=stderr)
        exit(1)
    try:
        lines = open(argv[1]).readlines()
        for line in lines:
            num = int(line)
            f1, f2 = fermat_factorisation(num)
            print("{}={}*{}".format(num, f1, f2))
    except FileNotFoundError as fnfe:
        print(fnfe)
