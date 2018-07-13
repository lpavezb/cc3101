#!/usr/bin/env python
    
def neg(s):
    return 's' if (s == 'c') else 'c'

# So for the first player's choice of 1-2-3
# the second player must choose (not-2)-1-2 
def p2(s):
    return neg(s[1]) + s[0] + s[1]


if __name__ == '__main__':
    print "-------------------------------------------------------------------------\n"
    options = ["c","s"]
    s = raw_input("ingrese input (ej: csc): ")

    if len(s) != 3:
    	print "\ninput incorrecto, debe ser secuencia de largo 3"
    else:
    	aux = True
    	for st in s:
    		if not st in options:
    			aux = False
    	if not aux:
    		print "\ninput incorrecto, la secuencia solo debe contener caracteres 's' o 'c'"
    	else:
    		print '\n' + p2(s)


    print "\n-------------------------------------------------------------------------"