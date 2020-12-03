import sys


graf = [x for x in open('day3_input.txt').read().splitlines()]

n = len(graf)

print(n)

import re

count = 0
import collections

M = len(graf[0])


y, count, ans = 0, 0, 1
for d in [1, 3, 5, 7]:
	count = 0
	y = 0
	for x in range(n):
		if graf[x][y % M] == '#':
			count += 1
		y += d
	ans *= count

for d in [1]:
	count = 0
	y = 0
	for x in range(0, n, 2):
		if graf[x][y % M] == '#':
			count += 1
		y += 1
	ans *= count
print(ans)
