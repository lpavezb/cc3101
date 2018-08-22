#!/usr/bin/env python

from Graph import *


class Tarea:
    def __init__(self):
        self.colors = {}
        self.g = Graph()

    def do_tarea(self, n, s):
        # transformar string a matriz con listas
        R = string_to_matrix(s)
        n = int(n)
        # agregar vertices al grafo e inicializar colores en n
        for i in range(1, n + 1):
            ind = str(i)
            self.colors[ind] = 'n'
            self.g.add_vertex(ind)

        # agregar conexiones al grafo
        for t in R:
            self.g.add_edge(t[0], t[1])

        # pintar grafo con 2 colores: a y r
        root = self.get_root()
        self.pintar(root, 'a')

        va = []
        vr = []
        # como el arbol es bipartito, separo los nodos por color en 2 listas
        for v in self.g.get_vertexs():
            if self.colors[v] == 'a':
                va.append(v)
            else:
                vr.append(v)

        # convertir el grafo dirigido a grafo simple
        for v in self.g.get_vertexs():
            for e in self.g.get_edge(v):
                self.g.add_edge(e, v)

        # reviso las conexiones que faltan entre va y vr
        aristas = 0
        for v in va:
            e = self.g.get_edge(v)
            for ver in vr:
                if ver not in e:
                    aristas += 1
        return aristas

    def pintar(self, v, c):
        # pintar si no tiene ningun color
        if self.colors[v] == 'n':
            self.colors[v] = c
            for n in self.g.get_edge(v):
                self.pintar(n, next_color(c))

    def get_root(self):
        # obtiene la raiz del arbol buscando el nodo que no tiene aristas apuntando hacia el
        ver = self.g.get_vertexs()
        for v in self.g.get_vertexs():
            for e in self.g.get_edge(v):
                ver.remove(e)
        return ver[0]


def next_color(s):
    if s == 'a':
        return 'r'
    else:
        return 'a'


def string_to_matrix(s):
    # este if es por la forma en que pruebo el programa, si lo hago sin raw_input, entonces
    # el string contiene \n, si lo hago con raw_input, entonces contiene //n
    if '\n' in s:
        l = s.split('\n')
    else:
        l = s.split('\\n')
    m = []
    for i in range(0, len(l)):
        m.append(l[i].split(" "))
    return m


print "-----------------------------------------------------"
print "ingrese numero de nodos en el arbol (enumerados de 1 a n): "
print "si se presiona enter sin ingresar numero se elige n=5"
n = raw_input("n: ")
if n == '':
    n = 5
print
print "\ningrese pares de nodos que representan aristas"
print "si se presiona enter sin ingresar matriz se elige 1 2\\n1 3\\n2 4\\n3 5"
s = raw_input("matriz: ")
if s == '':
    s = '1 2\n1 3\n2 4\n3 5'

t = Tarea()
print t.do_tarea(n, s)
print "-----------------------------------------------------"
