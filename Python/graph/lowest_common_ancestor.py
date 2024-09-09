# Created by loop0919 on 2024-09-09
# Copyright (c) 2024 RTWP

import math


class LowestCommonAncestor:
    """\
    Lowest Common Ancestor (LCA)
    ---
    木に対する最小共通祖先を求めるデータ構造
    """

    def __init__(self, n: int):
        """\
        木の頂点数 n を指定して初期化する
        Parameters:
            n (int): 木の頂点数
        """
        self._n = n
        self._logn = int(math.log2(self._n) + 2)
        self._depth = [0] * self._n
        self._distance = [0] * self._n
        self._ancestor = [[-1] * self._n for _ in range(self._logn)]
        self._edges = [[] for _ in range(self._n)]

    def add_edge(self, u: int, v: int, w: int = 1):
        """\
        u, v 間に重み w の辺を追加する
        Parameters:
            u (int): 辺の片方の頂点
            v (int): 辺のもう片方の頂点
            w (int): 辺の重み
        """
        self._edges[u].append((v, w))
        self._edges[v].append((u, w))

    def build(self, root: int = 0):
        """\
        根を root にした木を構築する
        Parameters:
            root (int): 根の頂点番号
        """
        stack = [root]

        while stack:
            now = stack.pop()
            for to, w in self._edges[now]:
                if self._ancestor[0][to] == now or self._ancestor[0][now] == to:
                    continue
                self._ancestor[0][to] = now
                self._depth[to] = self._depth[now] + 1
                self._distance[to] = self._distance[now] + w
                stack.append(to)

        for k in range(1, self._logn):
            for i in range(self._n):
                if self._ancestor[k - 1][i] == -1:
                    self._ancestor[k][i] = -1
                else:
                    self._ancestor[k][i] = self._ancestor[k - 1][self._ancestor[k - 1][i]]

    def lca(self, u: int, v: int) -> int:
        """\
        u, v の最小共通祖先を求める
        Parameters:
            u (int): 頂点 u
            v (int): 頂点 v
        Returns:
            lca (int): u, v の最小共通祖先
        """
        # u の深さを v の深さ以下になるよう調整する
        if self._depth[u] > self._depth[v]:
            u, v = v, u

        # v の深さを u に合わせる
        for k in range(self._logn - 1, -1, -1):
            if ((self._depth[v] - self._depth[u]) >> k) & 1 == 1:
                v = self._ancestor[k][v]

        # この時点で一致すれば、それが解
        if u == v:
            return u

        # u, v がギリギリ一致しないよう親方向に辿る
        for k in range(self._logn - 1, -1, -1):
            if self._ancestor[k][u] != self._ancestor[k][v]:
                u = self._ancestor[k][u]
                v = self._ancestor[k][v]

        # 最後に 1 ステップ親方向に辿った頂点が解
        return self._ancestor[0][u]

    def distance(self, u: int, v: int) -> int:
        """\
        u, v 間の距離を求める
        Parameters:
            u (int): 頂点 u
            v (int): 頂点 v
        Returns:
            dist (int): u, v 間の最短距離の長さ
        """
        return self._distance[u] + self._distance[v] - 2 * self._distance[self.lca(u, v)]

    def parent(self, v: int) -> int:
        """\
        v の親を求める
        Parameters:
            v (int): 頂点 v
        Returns:
            parent (int): 頂点 v の親
        """
        return self._ancestor[0][v]
