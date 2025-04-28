import copy

def FLOYD_WARSHALL(W):
    n = len(W)
    D_prev = copy.deepcopy(W)

    for k in range(n):
        D_curr = copy.deepcopy(D_prev)
        for i in range(n):
            for j in range(n):
                D_curr[i][j] = min(D_prev[i][j], D_prev[i][k] + D_prev[k][j])
        D_prev = D_curr

    return D_prev

INF = float('inf')

W = [
    [0, 5, INF, 30],
    [INF, 0, 5, 20],
    [INF, INF, 0, 5],
    [INF, INF, INF, 0]
]

D = FLOYD_WARSHALL(W)

vertex_names = ['A','B','C','D']

print("\n\nSolution:")
for i in range(len(D)):
    for j in range(len(D)):
        if D[i][j] == INF:
            print(f"{vertex_names[i]} → {vertex_names[j]}: INF", end="\t")
        else:
            print(f"{vertex_names[i]} → {vertex_names[j]}: {D[i][j]}", end="\t")
    print()