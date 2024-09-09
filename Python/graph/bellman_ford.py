# Created by loop0919 on 2024-09-09
# Copyright (c) 2024 RTWP

INF = float("inf")


def bellman_ford(start: int, graph: list[list[int]], check_negative_cycle: bool = True) -> list[int]:
    """\
    Bellman Ford 法
    ---
    Parameters:
        start (int): 始点の頂点番号
        graph (list[list[int]]): 隣接リスト
        check_negative_cycle (bool): 負閉路の検出を行うか
    
    Returns:
        dist (list[int]): 始点から各頂点への最短距離
    """
    n = len(graph)

    dist = [INF] * n
    dist[start] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[v] > dist[u] + w and dist[u] < INF:
                    dist[v] = dist[u] + w

    if not check_negative_cycle:
        return dist

    for _ in range(n):
        for u in range(n):
            for v, w in graph[u]:
                if dist[v] > dist[u] + w and dist[u] < INF:
                    dist[v] = -INF

    return dist
