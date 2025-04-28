class Vertex:
    def __init__(self, id):
        self.id = id
        self.d = float('inf')
        self.pi = None

class Graph:
    def __init__(self):
        self.V = []
        self.E = []
        self.w = {}

    def add_vertex(self, vertex):
        self.V.append(vertex)

    def add_edge(self, u, v, weight):
        self.E.append((u, v))
        self.w[(u, v)] = weight

def INITIALIZE_SINGLE_SOURCE(G, s):
    for v in G.V:
        v.d = float('inf')
        v.pi = None
    s.d = 0

def RELAX(u, v, w):
    if v.d > u.d + w[(u, v)]:
        v.d = u.d + w[(u, v)]
        v.pi = u

def BELLMAN_FORD(G, w, s):
    INITIALIZE_SINGLE_SOURCE(G, s)

    for i in range(len(G.V) - 1):
        for (u, v) in G.E:
            RELAX(u, v, w)
    
    for (u, v) in G.E:
        if v.d > u.d + w[(u, v)]:
            return False
    return True


G = Graph()
v0 = Vertex('s')
v1 = Vertex('t')
v2 = Vertex('x')
v3 = Vertex('y')
v4 = Vertex('z')

for v in [v0, v1, v2, v3, v4]:
    G.add_vertex(v)

G.add_edge(v0, v1, 6)
G.add_edge(v0, v3, 7)
G.add_edge(v1, v2, 5)
G.add_edge(v1, v3, 8)
G.add_edge(v1, v4, -4)
G.add_edge(v2, v1, -2)
G.add_edge(v3, v2, -3)
G.add_edge(v3, v4, 9)
G.add_edge(v4, v0, 2)
G.add_edge(v4, v2, 7)

has_no_negative_cycle = BELLMAN_FORD(G, G.w, v0)

print("\nBellman Ford Result:")
if has_no_negative_cycle:
    for v in G.V:
        print(f"Vertex {v.id}: Distance = {v.d}, Predecessor = {v.pi.id if v.pi else None}")
else:
    print("Graph contains a negative weight cycle!")
