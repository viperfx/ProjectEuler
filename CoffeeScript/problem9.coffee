for a in [1...1000]
  aa = a*a
  for b in [a...1000-a]
    bb = b*b
    c = 1000-a-b
    if aa + bb == c*c
      console.log a*b*c