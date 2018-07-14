#!/usr/bin/env python
    
def neg(s):
    return 's' if (s == 'c') else 'c'

# If the first player choice is s[0]-s[1]-s[2]
# the second player must choose (not-s[1])-s[0]-s[1] 
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