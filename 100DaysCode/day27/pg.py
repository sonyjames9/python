def add(*args):
  print(type(args))
  print(args[1])
  sum = 0
  for n in args:
    sum += n
  return sum

print(add(3,5,6,2,1,4))

def calculate(n, **kwargs):
  print(type(kwargs))

  for k,v in kwargs.items():
    print(k)
    
  n += kwargs["add"]
  print(n)    
  n += kwargs["multiply"]
  print(n)


calculate(2, add=3, multiply = 5)