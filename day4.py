import sys


a = [x for x in open('day4_input.txt').read().splitlines()]

n = len(a)

print(n)

import re

ans = 0
import collections

blocks = []

ans = 0

def validate(blocks):
	d = {}
	for x in blocks:
		items = x.split()
		for item in items:
			name, val = item.split(":")
			d[name] = val
	if not (len(d) == 8 or (len(d) == 7 and 'cid' not in d)):
		return
	if not (len(d["byr"]) == 4 and 1920 <= int(d["byr"]) <= 2002):
		return
	if not (len(d["iyr"]) == 4 and 2010 <= int(d["iyr"]) <= 2020):
		return
	if not (len(d["eyr"]) == 4 and 2020 <= int(d["eyr"]) <= 2030):
		return
	if d["hgt"].endswith("cm"):
		if not 150 <= int(d["hgt"][:-2]) <= 193:
			return
	elif d["hgt"].endswith("in"):
		if not 59 <= int(d["hgt"][:-2]) <= 76:
			return
	else:
		return
	hcl = d["hcl"]
	if not hcl.startswith("#"):
		return
	for x in hcl[1:]:
		if x not in "abcdef0123456789":
			return
	ecl = d["ecl"]
	if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
		return
	if len(d["pid"]) != 9:
		return
	for x in d["pid"]:
		if not x.isnumeric():
			return
	global ans
	ans += 1

for line in a:
	if line == "":
		validate(blocks)
		blocks = []
	else:
		blocks += [line]

if len(blocks) > 0:
	validate(blocks)

print(ans)
