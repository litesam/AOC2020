import sys


a = [x for x in open('day2_input.txt').read().splitlines()]

n = len(a)

print(n)

import re

count = 0
import collections

for line in a:
	a, b, c = line.split()

	left, right = map(int, a.split("-"))
	char = b[0]
	left -= 1
	right -=1

	#print(left, right, c, char)
	if c[left] == char and c[right] != char:
		count += 1
	elif c[left] != char and c[right] == char:
		count += 1

print(count)
