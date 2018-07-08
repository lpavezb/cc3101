#!/usr/bin/env python

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

def count_letters_and_reps(s):
    letters = []
    reps = {}
    for st in s:
        if not st in letters:
            letters.append(st)

    for let in letters:
        reps[let] = s.count(let)

    return letters, reps
    
def p1(s):
    l = len(s)

    letters, reps = count_letters_and_reps(s)

    delete = []
    aux = 1
    for let in letters:
        if reps[let]%2!=0:
            aux -= 1

    if aux<0: return 0
    num = fac(int(l/2))
    den = 1
    for let in letters:
        den *= fac(int(reps[let]/2))
    return num/den


if __name__ == '__main__':
    print "-------------------------------------------------------------------------\n"
    
    s = raw_input("ingrese input: ")
    print '\n' + str(p1(s))

    #print p1("aabbccaaddc")
    print "\n-------------------------------------------------------------------------"