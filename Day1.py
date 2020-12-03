import sys


a = []

while True:
	try:
		a += [int(input())]
	except ValueError:
		break

print(len(a))
for i in range(len(a)):
	for j in range(len(a)):
		for k in range(len(a)):
			if a[i] + a[j] + a[k] == 2020:
				print(a[i] * a[j] * a[k])
				import sys
				sys.exit(0)
