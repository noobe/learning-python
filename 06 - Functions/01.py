def testFunction():
  print("Hello from test function")

testFunction()

def testFunction2(val):
  print(val)

testFunction2('test value')

def testFunction3(val1, val2):
  print(val1, val2)

testFunction3('test value', 2)

def testFunction4(*vals):
  print(vals)

testFunction4('test', 1, True, ['arr'], {'key': 'val'})

def testFunction5(key1, key2):
  print(key1, key2)

testFunction5(key1='value1', key2='value2')

def testFunction6(**userData):
  print("The age of the user is "+userData['age'])

testFunction6(fname="AJ", age="33", lname="Xav")

def testFunction7(country = "USA"):
  print("The use is from " + country)

testFunction7()
testFunction7('India')

def testFunction8(val):
  return val*5

print(testFunction8(3))

def testFunction9():
  pass

testFunction9()

def testFunction10(k):
  if(k > 0):
    result = k + testFunction10(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
testFunction10(6)
