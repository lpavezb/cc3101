#!/usr/bin/env python
# Graph implementation obtained from http://www.forosdelweb.com/f130/aporte-sencilla-implementacion-grafos-817941/


class Graph:
    # Simple graph implementation:
    # Directed graph
    # Without weight in the edges
    # Edges can be repeated (se modifico para que no se repitieran)

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        # Add a vertex in the graph
        # Overwrite the value
        self.graph[vertex] = []

    def get_vertexs(self):
        # Get the vertexs in the graph
        return self.graph.keys()

    def del_vertex(self, vertex):
        # Remove the vertex if it's in the graph
        try:
            self.graph.pop(vertex)
        except KeyError:
            # Here vertex is not in graph
            pass

    def is_vertex(self, vertex):
        # Return True if vertex is in the graph
        # otherwise return False
        try:
            self.graph[vertex]
            return True
        except KeyError:
            return False

    def add_edge(self, vertex, edge):
        # Add a edge in vertex if vertex exists
        try:
            # grafo sin multiarcos
            if edge not in self.graph[vertex]:
                self.graph[vertex].append(edge)
        except KeyError:
            # Here vertex is no in graph
            pass

    def delete_edge(self, vertex, edge):
        # Remove a edge in vertex
        try:
            self.graph[vertex].remove(edge)
        except KeyError:
            # Here vertex is not in graph
            pass
        except ValueError:
            # Here the edge not exists
            pass

    def get_edge(self, vertex):
        # Return the edges of a vertex if the vertex is in the graph
        # Otherwise return None
        try:
            return self.graph[vertex]
        except KeyError:
            pass

    def __str__(self):
        # Print the vertex
        s = "Vertex -> Edges\n"
        for k, v in self.graph.iteritems():
            s += "%-6s -> %s\n" % (k, v)
        return s
