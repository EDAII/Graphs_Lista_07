import heapq
from math import sin, cos, sqrt, atan2, radians
from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertex_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vertex_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, vertex_name):
        if vertex_name in self.vertex_dict:
            return self.vertex_dict[vertex_name]
        else:
            return None

    def add_edge(self, origin, destination, cost=0):
        if origin not in self.vertex_dict:
            self.add_vertex(origin)
        if destination not in self.vertex_dict:
            self.add_vertex(destination)

        self.vertex_dict[origin].add_neighbor(self.vertex_dict[destination], cost)
        self.vertex_dict[destination].add_neighbor(self.vertex_dict[origin], cost)
