from networkx import random_regular_graph
from random import sample

def generate_isomorphism(g):
    vertices = set([])
    for e in g.edges():
        vertices.add(e[0])
        vertices.add(e[1])

    mapped_vertices = {}
    edges = []
    for e in g.edges():
        new_edge = []
        for i in [0, 1]:
            if e[i] not in mapped_vertices:
                replacement = sample(vertices, 1)[0]
                vertices.remove(replacement)
                mapped_vertices[e[i]] = replacement
            else:
                replacement = mapped_vertices[e[i]]
                
            new_edge.append(replacement)
        edges.append(tuple(new_edge))
    return sorted(edges)

k = 10

g = random_regular_graph(k, 2*k+1)

for i in range(100000):
    print(1, ",".join(map(str, generate_isomorphism(g))))

for i in range(1000):
    print(0, random_regular_graph(k, 2*k+1))
