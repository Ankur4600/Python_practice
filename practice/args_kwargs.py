# *args and **kwargs

def super_func (*args, **kwargs):
  total = 0
  print(*args)
  print(kwargs)
  for value in kwargs.values():
    total+=value
  return sum(args) +total
print(super_func(1,2,3,4,5,6, arg1=55, arg2=55))