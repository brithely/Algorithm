class Vertex:
    def __init__(self, name):
        self.name = name
        self.vertices = list()

    def __repr__(self):
        return f"{self.name}"


class Graph:
    def add_edge(self, vertex1, vertex2):
        vertex1.vertices.append(vertex2)
        vertex2.vertices.append(vertex1)

    def get_nearby_vertices(self, vertex, distance) -> list:
        nearby_vertices = []
        all_nearby_vertices = []
        depth = 1
        nearby_vertices.append(vertex.vertices)
        all_nearby_vertices += vertex.vertices
        while depth < distance:
            print(depth, nearby_vertices[depth - 1])
            depth_vertices = list()
            for nearby_vertex in nearby_vertices[depth - 1]:
                temp_vertices = [
                    i
                    for i in nearby_vertex.vertices
                    if i != vertex and i not in all_nearby_vertices
                ]
                depth_vertices += temp_vertices
                all_nearby_vertices += temp_vertices
            nearby_vertices.append(depth_vertices)
            depth += 1
        return all_nearby_vertices


g = Graph()
v1 = Vertex("1")
v2 = Vertex("2")
v3 = Vertex("3")
v4 = Vertex("4")
v5 = Vertex("5")
v6 = Vertex("6")
v7 = Vertex("7")
g.add_edge(v1, v2)
g.add_edge(v1, v2)
g.add_edge(v1, v4)
g.add_edge(v1, v7)
g.add_edge(v2, v3)
g.add_edge(v2, v5)
g.add_edge(v3, v6)
g.add_edge(v5, v6)
g.add_edge(v5, v5)
g.add_edge(v5, v7)
g.add_edge(v4, v7)
g.add_edge(v7, v6)

v = g.get_nearby_vertices(v5, 3)
print(v)
