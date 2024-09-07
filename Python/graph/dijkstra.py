from heapq import heappop, heappush

INF = float("inf")


def dijkstra(start: int, graph: list[list[int]]) -> list[int]:
    """\
    Dijkstra 法
    ---
    Parameters:
        start (int): 始点の頂点番号
        graph (list[list[int]]): 隣接リスト
    Returns:
        dist (list[int]): 始点から各頂点への最短距離
    """
    n = len(graph)

    dist = [INF] * n
    dist[start] = 0

    checked = [False] * n

    pq = [(0, start)]

    while len(pq) > 0:
        now_d, now_v = heappop(pq)

        if checked[now_v]:
            continue

        checked[now_v] = True

        for next_v, cost in graph[now_v]:
            if checked[next_v]:
                continue

            next_d = now_d + cost

            if next_d >= dist[next_v]:
                continue

            dist[next_v] = min(next_d, dist[next_v])
            heappush(pq, (next_d, next_v))

    return dist
