#!/usr/bin/env python

def p1(s):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    const = "a"
    var   = "b"
    par   = "c"
    su    = "d"
    mult  = "e"

    res = ""

    if not arit(s):
        return "NO\n"

    pars = countBrackets(s)
    if pars == "NO\n":
        return pars

    res += par*pars # agrega parentesis
    res += const*countConsts(s) # agrega constantes
    res += su*s.count("+") # agrega sumas
    res += mult*s.count("*") # agrega multiplicaciones

    for a in s: # agrega variables, suponiendo que cada variable esta compuesta por una letra
        if a in letters:
            res += var

    res = ''.join(sorted(res)) # ordena respuesta final alfabeticamente
    return res

def arit(s):
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

    l = s.split("*")
    if '' in l:
        return False
    d = True
    for st in l:
        c = False
        if st[0] == '+' or st[len(st) - 1] == '+': return False
        for a in st:
            if a in letters or a in num:
                c = True
        d = d and c
    return b and d

def countConsts(s):
    num = "1234567890"

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
    return n

def countBrackets(s):
    pars = 0
    for a in s:
        if a == "(":
            pars += 1
        if a == ")":
            pars -= 1
        if pars < 0:
            return "NO\n"
    if pars == 0:
        return s.count("(")
    else:
        return "NO\n"


def test(In, Out):
    file_in  = open(In,"r")
    file_out = open(Out,"r")

    f = 0
    for line in file_out:
        line_in = file_in.readline() 

        if line == "NO\n":
            res = "NO\n"
        else: 
            # ordena alfabeticamente 
            res = line.replace(",","").replace("\n","")
            res = ''.join(sorted(res))

        bol = p1(line_in) == res
        if not bol:
            print line_in
            f+=1
    print "Errores: " + str(f)





if __name__ == '__main__':
    print "-------------------------------------------------------------------------"
    b = input("probar con un string / probar con archivos con input-outputs [0/1]: ")
    print "-------------------------------------------------------------------------"
    if b==0:
        #s = "(90*r+b+(l*y)*95)*j*b*((g*51)+x)+29+g"
        s = raw_input("ingrese string: ")
        print "-------------------------------------------------------------------------"
        print p1(s)
    else:
        In = raw_input("ingrese nombre de archivo con inputs (ej: Arit_In.txt): ")
        Out = raw_input("ingrese nombre de archivo con outputs (ej: Arit_Out.txt): ")
        print "-------------------------------------------------------------------------"
        test(In, Out)
    
    print "-------------------------------------------------------------------------"