#!/usr/bin/env python
 
import numpy as np

def p4_b(n):
    l = 2**n
    res = np.zeros((l, l))
    b = True
    for i in range(0, l):
        for j in range(0, l):
            if b:
                res[i][j] = 1
            b = not b
        b = not b
    return toString(res)

def toString(m):
    res = ""
    l = np.shape(m)[0]
    for i in range(0, l):
        for j in range(0, l):
            if m[i][j] == 1:
                res += '1'
            else:
                res += '0'
            res += ' '
        res += '\n'
    return res

if __name__ == '__main__':
    print "----------------------------------------------------"

    n = input('n: ' )
    print p4_b(n)
    
    print "----------------------------------------------------"