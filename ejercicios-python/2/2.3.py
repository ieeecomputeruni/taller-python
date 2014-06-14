
lis = range(0,121)[::10]

for f in lis:
	c = (f - 32) * (5.0 / 9)
	print "%f Farenheit = %f Centigrados" %(f,c)
	