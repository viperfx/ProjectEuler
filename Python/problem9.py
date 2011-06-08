import math

def triplet(a,b):
	first= a**2
	second= b**2
	third1= first+second
	third2= math.sqrt((first+second))
	if third1 == third2**2:
		print "this is a triplet"

if __name__ == '__main__':
	#triplet(3,4)
	for a in range(1,1000):
		aa = a*a
		for b in range(1,1000-a):
			bb = b*b
			c = 1000-a-b
			if aa+bb == c*c:
				print a*b*c