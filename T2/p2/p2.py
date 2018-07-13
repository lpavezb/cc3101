#!/usr/bin/env python
    
def neg(s):
    res = 's' if s == 'c' else 'c'
    return res

# So for the first player's choice of 1-2-3
# the second player must choose (not-2)-1-2 
def p2(s):
    return neg(s[1]) + s[0] + s[1]


if __name__ == '__main__':
    print "-------------------------------------------------------------------------\n"
    
    s = raw_input("ingrese input (ej: ccc): ")
    print '\n' + p2(s)

    print "\n-------------------------------------------------------------------------"