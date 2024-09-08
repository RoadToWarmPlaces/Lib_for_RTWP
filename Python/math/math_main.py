# Created by hiro1729 on 2024-09-08
# Copyright (c) 2024 RTWP

from typing import List
from math import *

# O(sqrt(N))
def isprime_slow(N: int):
	if N == 1:
		return False
	if N == 2:
		return True
	for i in range(2, isqrt(N) + 1):
		if N % i == 0:
			return False
	return True

# O(sqrt(N))
def divisors(N: int):
	divisors = []
	for i in range(1, isqrt(N) + 1):
		if N % i == 0:
			divisors.append(i)
			if i * i != N:
				divisors.append(N // i)
	divisors.sort()
	return divisors

# O(N)
def linear_sieve(N: int):
	lpf = [-1] * (N + 1)
	prime_list = []
	for d in range(2, N + 1):
		if lpf[d] == -1:
			lpf[d] = d
			prime_list.append(d)
		for p in prime_list:
			if p * d > N or p > lpf[d]:
				break
			lpf[p * d] = p
	return (lpf, prime_list)

# please call linear_sieve(N) before calling this
# O(log(N))
def prime_factorize_sieve(N: int, lpf: List[int]):
	prime_factors = []
	while N > 1:
		prime_factors.append(lpf[N])
		N //= lpf[N]
	return prime_factors

# O(sqrt(N))
def prime_factorize(N: int):
	M = isqrt(N)
	prime_factors = []
	for i in range(2, M + 1):
		if i > M:
			break
		if N % i == 0:
			while N % i == 0:
				prime_factors.append(i)
				N //= i
			M = isqrt(N)
	if N > 1:
		prime_factors.append(N)
	return prime_factors
