# Created by hiro1729 on 2024-09-14
# Copyright (c) 2024 RTWP

class UnionFind:
	def __init__(self, N):
		self.N = N
		self.P = [-1] * N

	def leader(self, u):
		if self.P[u] == -1:
			return u
		v = self.P[u]
		while self.P[v] != -1:
			self.P[u] = self.P[v]
			u = v
			v = self.P[v]
		return self.P[u]

	def merge(self, u, v):
		u = self.leader(u)
		v = self.leader(v)
		if u == v:
			return
		self.P[u] = v

	def same(self, u, v):
		return self.leader(u) == self.leader(v)