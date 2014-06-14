
n = input("ingrese un numero")


#forma 1
for x in range(1,n+1):
	print x, " - ",(x * (x+1)) / 2


#forma 2

def suma(n):
	s = 0
	for x in range(1,n+1):s += x
	return s

for y in range(1,n+1):
	print y, " - ", suma(y)

