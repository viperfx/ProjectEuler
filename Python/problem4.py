"""
Palindrome of 3 digit number
"""

l = []
for n1 in range(100,999):
	for n2 in range(100,999):
		t = n1*n2
		string = str(t)
		reverse = string[::-1]
		if string == reverse:
			#print string+" is a palindrome"
			l.append(t)
print max(l)