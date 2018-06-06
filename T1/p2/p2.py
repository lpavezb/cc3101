#!/usr/bin/env python


###################### PARTE a ######################

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



###################### PARTE c ######################


def p2_c(s):
    R = stringToMatrix(s)
    return matrixToString(RinterRinv(R))

def RinterRinv(R):
    l = len(R)
    res = []
    Rinv = inv(R)

    for i in range(0, l):
        res.append(['0' for i in range(0, l)])
    for i in range(0, l):
        for j in range(0, l):
            if R[i][j] == Rinv[i][j] == '1':
                res[i][j] = '1'
    return res


def inv(R):
    l = len(R)
    res = []
    for i in range(0, l):
        res.append(['0' for i in range(0, l)])
    for i in range(0, l):
        for j in range(0, l):
            if R[i][j] == '1':
                res[j][i] = '1'
    return res


###################### MISC ######################

def stringToMatrix(s):
    l = s.split("\n")
    m = []
    for i in range(0, len(l)):
        m.append(l[i].split(" "))
    return m

def matrixToString(M):
    res = ""
    l = len(M)
    for i in range(0, l):
        for j in range(0, l):
            res += M[i][j] + " "
        res += '\n'
    return res


if __name__ == '__main__':
    print "-----------------------------------------------------"
    print "--------------------- test p2_a ---------------------\n"

    print p2_a("1 0 0\n0 1 0\n0 0 1")

    print "\n-----------------------------------------------------"
    print "--------------------- test p2_c ---------------------\n"

    print p2_c("1 1 1\n0 1 1\n0 1 1")

    print "-----------------------------------------------------"