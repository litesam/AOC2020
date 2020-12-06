import sys


a = [x for x in open('day5_input.txt').read().splitlines()]

n = len(a)

print("len:", n)

import re

ans = 0
import collections

s = set()
mx = 0
for line in a:
	left = 0
	right = 127
	for x in line[:-3]:
		mid = (left + right) // 2

		if x == 'F':
			right = mid
		else:
			left = mid

	left2 = 0
	right2 = 7

	for x in line[-3:]:
		mid = (left2 + right2) // 2
		if x == 'R':
			left2 = mid
		else:
			right2 = mid
	left += 1
	left2 += 1
	#print(left, left2, left * 8 + left2)
	mx = max(mx, left * 8 + left2)
	s.add(left * 8 + left2)
#print(mx)
for x in range(mx + 1000):
	if (x % 8 > 0) and (x - 1 in s) and (x not in s) and (x + 1 in s):
		print(x)
		break
