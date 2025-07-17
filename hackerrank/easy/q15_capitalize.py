import math
import os
import random
import re
import sys

def solve(s):
    parts = s.split(' ')
    ans = []
    for p in parts:
        if p == '':
            ans.append('')
        else:
            first = p[0]
            rest = p[1:]
            if 'a' <= first <= 'z':
                first = chr(ord(first) - 32)
            ans.append(first + rest)
    return ' '.join(ans)






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
