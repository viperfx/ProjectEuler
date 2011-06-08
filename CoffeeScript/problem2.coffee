# sum of even fibonacci numbers up to 4M
answer = 0
[f,s,t] = [0,1,1]

while t <= 4000000
  [f,s,t] = [s,t,s+t]
  if t % 2 == 0
    answer += t

console.log answer

