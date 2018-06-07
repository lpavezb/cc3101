#!/usr/bin/env python

from Graph import *

def sat_2cnf(F):
    graph = Graph()

    fill_graph(graph, F)

    keys = graph.get_vertexs()
    for key in keys:
        p1 = graph.find_path(key, neg(key))
        p2 = graph.find_path(neg(key), key)
        if p1 != None and p2 != None:
            return 0
    return 1
        
def sat_dnf(F):
    l = F.replace('(', '').replace(')', '').split('o')
    for c in l:
        n = c.split('y')
        for v in n:
            if neg(v) in n:
                return 0
    return 1

def fill_graph(graph, F):
    l = F.replace('(', '').replace(')', '').split('y')

    v = []
    for c in l:
        n = c.split('o')
        A = n[0]
        B = n[1]
        add_v(neg(A), v, graph)
        add_v(neg(B), v, graph)
        graph.add_edge(neg(A), B)
        graph.add_edge(neg(B), A)

def add_v(ver, v, graph):
    if not ver in v:
        graph.add_vertex(ver)
        v.append(ver)

def neg(v):
    if v[0] == '-':
        return v[1:]
    else:
        return '-' + v


if __name__ == '__main__':
    print "-----------------------------------------------------"
    print "--------------------- test cnf ---------------------\n"

    print sat_2cnf("(x1ox2)y(-x2ox3)y(-x1o-x2)y(x3ox4)y(-x3ox5)y(-x4o-x5)y(-x3ox4)")
    #print sat_2cnf("(-x1ox5)y(-x5o-x1)y(x2ox4)y(x1ox3)y(-x3ox1)")

    print "\n-----------------------------------------------------"
    print "--------------------- test dnf ---------------------\n"

    print sat_dnf("(x1y-x2)o(x2y-x1yx4)o(-x4y-x3yx1)")

    print "\n-----------------------------------------------------"