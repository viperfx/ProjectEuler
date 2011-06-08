f=[1,2]
n=2
t=0
sum=0
while t <= 4000000:
	t = f[n-1]+f[n-2]
	n += 1
	f.append(t)
print f
for n in range(0,len(f)):
	if f[n]%2==0:
		sum = sum+f[n]
print sum
"""
a, b = 0,1
f = []
while b < 4000000:
	f.append(b)
	a,b = b, a+b
print f
"""