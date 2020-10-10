#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):   #0 0 1 0 0 1 0
    n = len(c)
    jmp = 0
    while n > 1:
        if n != 2:
            if c[1] == 0 and c[2] == 0:

                jmp += 1
                c[:2] = ''
                n -= 2
            elif c[1] == 1 and c[2] == 0:
                jmp += 1
                c[:2] = ''
                n -= 2
            else:
                c[:1] = ''
                jmp += 1
                n -= 1


        else:
            if c[1] == 0:
                c[:1] = ''
                jmp += 1
                n -= 1
            n -= 1

    return jmp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
