#!/usr/bin/env python
import numpy as np


def do_tarea(m, k, par):
    mk = pow(m, k)
    return int(mk[par[0]][par[1]])


def pow(m, k):
    if k == 1:
        return m
    tmp = pow(m, k/2)
    res = tmp.dot(tmp)
    if k % 2 == 0:
        return res
    else:
        return res.dot(m)


def string_to_matrix(s, n):
    # este if es por la forma en que pruebo el programa, si lo hago sin raw_input, entonces
    # el string contiene \n, si lo hago con raw_input, entonces contiene //n
    if '\n' in s:
        l = s.split('\n')
    else:
        l = s.split('\\n')
    m = []
    for i in range(0, len(l)):
        m.append(l[i].split(" "))
    res = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            if m[i][j] == '1':
                res[i][j] = 1
    return res


print "-----------------------------------------------------"
print "ingrese numero de nodos en el arbol (enumerados de 1 a n): "
print "si se presiona enter sin ingresar numero se elige n=5"
n = raw_input("n: ")
if n == '':
    n = 5
n = int(n)
print
print "\ningrese matriz de adyacencia"
print "si se presiona enter sin ingresar matriz se elige 0 0 1 0 1\\n0 0 1 0 0\\n1 1 0 1 0\\n0 0 1 0 0\\n1 0 0 0 0"
m = raw_input("matriz: ")
if m == '':
    m = '0 0 1 0 1\n0 0 1 0 0\n1 1 0 1 0\n0 0 1 0 0\n1 0 0 0 0'

print
print "ingrese k: "
print "si se presiona enter sin ingresar k se elige k=2"
k = raw_input('k: ')
if k == '':
    k = 2
k = int(k)
print
print "ingrese par u, v: "
print "si se presiona enter sin ingresar par se elige (u, v) = 0 3"
par = raw_input('u v: ')
if par == '':
    par = '0 3'
p = par.split(' ')
p[0] = int(p[0])
p[1] = int(p[1])

matriz = string_to_matrix(m, n)
print
print 'respuesta: ' + str(do_tarea(matriz, k, p))
print "-----------------------------------------------------"
