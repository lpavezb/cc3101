#!/usr/bin/env python

def p1(s):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    var   = "b"
    su    = "d"
    mult  = "e"

    res = ""


    res += countBrackets(s)
    if res == "NO\n":
        return res

    if not aritSum(s) or not aritMult(s):
        return "NO\n"

    res += countConsts(s)

    res += su*s.count("+")
    res += mult*s.count("*")

    for a in s:
        if a in letters:
            res += var

    res = ''.join(sorted(res))
    return res

def aritSum(s):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    num = "1234567890"
    l = s.split("+")
    if '' in l:
        return False
    b = True
    for st in l:
        c = False
        if st[0] == '*' or st[len(st) - 1] == '*': return False
        for a in st:
            if a in letters or a in num:
                c = True
        b = b and c
    return b

def aritMult(s):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    num = "1234567890"
    l = s.split("*")
    if '' in l:
        return False
    b = True
    for st in l:
        c = False
        if st[0] == '+' or st[len(st) - 1] == '+': return False
        for a in st:
            if a in letters or a in num:
                c = True
        b = b and c
    return b

def countConsts(s):
    const = "a"
    num = "1234567890"
    res = ""

    n = 0
    i = 0
    l = len(s)
    while i<l:
        if s[i] in num:
            n += 1
            try:
                while s[i+1] in num:
                    i += 1
            except Exception as e:
                pass
        i += 1
    res += const*n
    return res

def countBrackets(s):
    par   = "c"
    res = ""

    pars = 0
    for a in s:
        if a == "(":
            pars += 1
        if a == ")":
            pars -= 1
        if pars < 0:
            return "NO\n"
    if pars == 0:
        res += par*s.count("(")
    else:
        return "NO\n"
    return res


def test():
    file_in  = open("Arit_In.txt","r")
    file_out = open("Arit_Out.txt","r")
    f = 0
    for line in file_out:
        line_in = file_in.readline() 

        if line == "NO\n":
            res = "NO\n"
        else:
            res = line.replace(",","").replace("\n","")
            res = ''.join(sorted(res))

        bol = p1(line_in) == res
        if not bol:
            print line_in
            f+=1
        print bol

    print f

if __name__ == '__main__':
    print "----------------------------------------------------"

    test()
    
    print "----------------------------------------------------"

    