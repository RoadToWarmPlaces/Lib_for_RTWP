# Created by Yuyo1984 on 2024-09-11
# Copyright (c) 2024 RTWP

# グラフの構築、及びBFSのために導入
from collections import defaultdict as dd
from collections import deque as dq

# 上下左右の探索のため定義（順番は右上左下）
mv_x = (1, 0, -1, 0)
mv_y = (0, -1, 0, 1)

INF = 2 << 60


# グラフのクラス
class Graph:
    # 初期化
    def __init__(self):
        self.graph = dd(set)
        self.removed_nodes = dd(set)
        self.removed_edges = set()

    # 無向エッジの追加
    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    # 有向エッジの追加
    def add_edge2(self, u, v):
        self.graph[u].add(v)

    # ノードの削除
    def remove_node(self, node):
        if node in self.graph:
            self.removed_nodes[node] = self.graph.pop(node)
            for neighbor in self.removed_nodes[node]:
                self.graph[neighbor].remove(node)

    # ノードの復元
    def restore_node(self, node):
        if node in self.removed_nodes:
            self.graph[node] = self.removed_nodes.pop(node)
            for neighbor in self.graph[node]:
                self.graph[neighbor].add(node)

    # エッジの削除
    def remove_edge(self, node1, node2):
        edge = tuple(sorted((node1, node2)))
        if edge not in self.removed_edges:
            self.graph[node1].remove(node2)
            self.graph[node2].remove(node1)
            self.removed_edges.add(edge)

    # エッジの復元
    def restore_edge(self, node1, node2):
        edge = tuple(sorted((node1, node2)))
        if edge in self.removed_edges:
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)
            self.removed_edges.remove(edge)

    # 見てるノードに隣接してるノードを取得
    def get_neighbor(self, node):
        return self.graph[node]

    # 幅優先探索(始点からの最短経路長を返す)
    def bfs_getdist(self, start, dist):
        dist[start] = 0
        que = dq([start])

        while que:
            node = que.popleft()
            for neighbor in self.graph[node]:
                if dist[neighbor] == INF:
                    dist[neighbor] = dist[node] + 1
                    que.append(neighbor)

        return dist

    # 幅優先探索(最短経路がいくつあるか)
    def bfs_cntshortest(self, start, goal):
        dist = dd(lambda: INF)
        ways = dd(int)

        dist[start] = 0
        ways[start] = 1

        que = dq([start])

        while que:
            node = que.popleft()
            for neighbor in self.graph[node]:
                if dist[neighbor] == INF:
                    dist[neighbor] = dist[node] + 1
                    que.append(neighbor)

                if dist[neighbor] == dist[node] + 1:
                    ways[neighbor] += ways[node]

        return ways[goal]

    # 幅優先探索(グラフが連結か判定)
    def bfs_connected(self, start):
        visited = set()
        que = dq([start])
        visited.add(start)

        while que:
            node = que.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    que.append(neighbor)

        return len(visited) == len(self.graph)

    def is_connected(self):
        if not self.graph:
            return True

        start = next(iter(self.graph))
        return self.bfs_connected(start)


# グリッドをグラフにする関数
def grid_to_graph(grid):
    # 行の長さと列の長さを変数にする。
    rows, cols = len(grid), len(grid[0])
    graph = Graph()

    for i in range(rows):
        for j in range(cols):
            # もし、今見てるマスが空きマスなら
            if grid[i][j] == ".":
                # 上下左右を見て、グリッド上にある＆空きマスなら
                for k in range(4):
                    mi = i + mv_x[k]
                    mj = j + mv_y[k]
                    if 0 <= mi < rows and 0 <= mj < cols and grid[mi][mj] == ".":
                        # 二次元配列のインデックスを一次元に落としてエッジを追加
                        u = i * cols + j
                        v = mi * cols + mj
                        graph.add_edge(u, v)

    return graph


# 以下具体例（ABC007-C）
def main():
    # r, c = map(int, input().split())
    # start = list(map(lambda x: int(x) - 1, input().split()))
    # goal = list(map(lambda x: int(x) - 1, input().split()))
    # grid = [list(input()) for _ in range(r)]
    # graph = grid_to_graph(grid)

    # 取得したい距離を一次元配列で持っておく（初期値はINFで）
    # dist = [INF for _ in range(r * c + 1)]
    # start = start[0] * c + start[1]
    # res = graph.bfs_getdist(start, dist)

    # idx = goal[0] * c + goal[1]
    # ans = res[idx]
    # print(ans)

if __name__ == "__main__":
    main()
