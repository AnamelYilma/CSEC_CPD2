import sys
from collections import deque

n = int(sys.stdin.readline())
col = [0] + list(map(int, sys.stdin.readline().split()))
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

comp = [0] * (n+1)
cid = 0
for i in range(1, n+1):
    if not comp[i]:
        cid += 1
        stack = [i]
        comp[i] = cid
        while stack:
            u = stack.pop()
            for v in g[u]:
                if not comp[v] and col[u] == col[v]:
                    comp[v] = cid
                    stack.append(v)

adj = [[] for _ in range(cid+1)]
for u in range(1, n+1):
    for v in g[u]:
        if comp[u] != comp[v]:
            adj[comp[u]].append(comp[v])

def bfs(start):
    dist = [-1] * (cid+1)
    q = deque([start])
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

if cid == 1:
    print(0)
else:
    d1 = bfs(1)
    u = max(range(1, cid+1), key=lambda i: d1[i])
    d2 = bfs(u)
    diam = max(d2[1:])
    print((diam + 1) // 2)
