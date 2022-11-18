i = 1
while i < 6:
  print(i)
  i += 1


j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1

k = 0
while k < 6:
  k += 1
  if k == 3:
    continue
  print(k)

l = 1
while l < 6:
  print(l)
  l += 1
else:
  print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass