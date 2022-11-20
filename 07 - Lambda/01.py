multiplyTen = lambda a : a*10
print(multiplyTen(3))

def multiplier(n):
  return lambda a : a*n

doubler = multiplier(2)
print(doubler(3))