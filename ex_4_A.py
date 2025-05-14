import heapq

def dijkstra(n, _, edges):
    g = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    pr = [0] * (n + 1)

    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))

    dist[1] = 0
    heap = [(0, 1)]

    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue

        for v, w in g[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pr[v] = u
                heapq.heappush(heap, (dist[v], v))

    return dist, pr


def path_print(n, pr):
    path = []
    v = n
    while v:
        path.append(v)
        v = pr[v]

    for node in reversed(path):
        print(node, end=' ')

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    dist, pr = dijkstra(n, m, edges)

    if dist[n] == float('inf'):
        print("-1")
    else:
        path_print(n, pr)



if __name__ == "__main__":
    main()