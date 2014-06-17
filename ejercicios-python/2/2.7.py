
a = []
b = []

n = int (input("Ingrese n: "))

for x in range(n+1) :
	a.append(x)
	b.append(x)

m = 0

while m <= n :
	for x in range(m,n+1) :
		for y in range(m,n+1) :
			print a[x], " - ",b[y]
		break
	m = m + 1

