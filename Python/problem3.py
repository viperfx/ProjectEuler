"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

factors = []
n = 600851475143
lastresult = n

while True:
    if lastresult == 1:
        break

    c = 2

    while True:
        if lastresult % c == 0:
            break

        c += 1

    factors.append(c)
    lastresult /= c

print factors