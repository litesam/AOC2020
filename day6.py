import sys


a = [x for x in open('day6_input.txt').read().splitlines()]

n = len(a)

print("len:", n)

ans = 0
members = 0

blocks = ""
def solve_one():
	part1 = False
	alphas = [0] * 26
	for alpha in blocks:
		num = ord(alpha) - ord('a')
		alphas[num] += 1
	global ans
	global members
	if part1 == True:
		ans += sum(alphas)
	else:
		has = []
		for al in alphas:
			if al == members:
				has += [al]
		ans += len(has)


for splits in a:
	if splits == '':
		solve_one()
		blocks = ''
		members = 0
	else:
		blocks += splits
		members += 1
if blocks:
	solve_one()

print(ans)
