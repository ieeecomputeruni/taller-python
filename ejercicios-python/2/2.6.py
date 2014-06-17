
a = [0,1,2,3,4,5,6]
b = [0,1,2,3,4,5,6]
m = 0


while m <= 6 :
	for x in range(m,7) :
		for y in range(m,7) :
			print a[x], " - ",b[y]
		break
	m = m + 1

