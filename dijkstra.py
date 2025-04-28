import heapq

class Vertex:
    def __init__(self, id):
        self.id = id
        self.d = float('inf')
        self.pi = None

    def __lt__(self, other):
        return self.d < other.d

class Graph:
    def __init__(self):
        self.V = []
        self.Adj = {}
        self.w = {}

    def add_vertex(self, vertex):
        self.V.append(vertex)
        self.Adj[vertex] = []

    def add_edge(self, u, v, weight):
        self.Adj[u].append(v)
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

def DIJKSTRA(G, w, s):
    INITIALIZE_SINGLE_SOURCE(G, s)
    S = []
    Q = G.V.copy()
    heapq.heapify(Q)

    while Q:
        u = heapq.heappop(Q)
        S.append(u)
        for v in G.Adj[u]:
            RELAX(u, v, w)
        heapq.heapify(Q)
    
    return S


G = Graph()

vertices = {}
for name in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    vertices[name] = Vertex(name)
    G.add_vertex(vertices[name])

G.add_edge(vertices['A'], vertices['B'], 4)
G.add_edge(vertices['A'], vertices['C'], 3)
G.add_edge(vertices['A'], vertices['E'], 7)
G.add_edge(vertices['B'], vertices['C'], 6)
G.add_edge(vertices['B'], vertices['D'], 5)
G.add_edge(vertices['C'], vertices['D'], 11)
G.add_edge(vertices['C'], vertices['E'], 8)
G.add_edge(vertices['D'], vertices['E'], 2)
G.add_edge(vertices['D'], vertices['F'], 2)
G.add_edge(vertices['D'], vertices['G'], 10)
G.add_edge(vertices['E'], vertices['G'], 5)
G.add_edge(vertices['F'], vertices['G'], 3)

source = vertices['A']
result = DIJKSTRA(G, G.w, source)


print("\n\nUsing dijkstra, we get: ")
for v in result:
    path = []
    current = v
    while current:
        path.append(current.id)
        current = current.pi
    path = path[::-1]
    print(f"Vertex {v.id}: Distance = {v.d}, Path = {' -> '.join(path)}")