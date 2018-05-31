#!/usr/bin/env python
 
def p2_a(s):
    #cuasi orden: refleja y transitiva
    R = stringToMatrix(s)

    if refleja(R) and transitiva(R):
        return 1
    return 0


def refleja(R):
    #refleja: R(i, i) = 1
    res = True
    n = len(R)
    #recorre matriz triangular superior
    for i in range(0, n):
        if R[i][i] == '0':
            res = False
            break
    return res

def transitiva(R):
    #transitiva: if R(i, j) and R(j, k) => R(i, k)
    res = True
    n = len(R)
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                if (R[i][j] == '1') and (R[j][k] == '1') :
                    if R[i][k] != '1' :
                        res = False
                        break;
    return res

def stringToMatrix(s):
    l = s.split("\n")
    m = []
    for i in range(0, len(l)):
        m.append(l[i].split(" "))
    return m

if __name__ == '__main__':
    print "----------------------------------------------------"

    print p2_a("1 0 0\n0 1 0\n0 0 1")
    
    print "----------------------------------------------------"