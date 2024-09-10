# Created by Yuyo1984 on 2024-09-09
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
        self.graph = dd(list)

    # エッジの追加
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # 幅優先探索
    def bfs(self, start, dist):
        dist[start] = 0
        que = dq([start])

        while que:
            node = que.popleft()
            for neighbor in self.graph[node]:
                if dist[neighbor] == INF:
                    dist[neighbor] = dist[node] + 1
                    que.append(neighbor)

        return dist


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
    r, c = map(int, input().split())
    start = list(map(lambda x: int(x) - 1, input().split()))
    goal = list(map(lambda x: int(x) - 1, input().split()))
    grid = [list(input()) for _ in range(r)]
    graph = grid_to_graph(grid)

    # 取得したい距離を一次元配列で持っておく（初期値はINFで）
    dist = [INF for _ in range(r * c + 1)]
    start = start[0] * c + start[1]
    res = graph.bfs(start, dist)

    idx = goal[0] * c + goal[1]
    ans = res[idx]
    print(ans)


if __name__ == "__main__":
    main()
