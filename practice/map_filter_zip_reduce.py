from functools import reduce

#map => map(function, iterable)
item_list = [9,8,7,6,5,]

def multiply_by2 (item):
  return item*2

print(list(map(multiply_by2,item_list)))
print(list(map(multiply_by2,[1,2,3,4])))





#filter => filter(function, iterable)

def only_even (item):
  return item % 2 == 0

print(list(filter(only_even,item_list))) 




#zip => zip(list1,list2) return touple using both

list1 =[1,2,3,4,5,6,7]
list2 = [9,8,7,6,5,4]
print(list(zip(list1,list2)))





def accumulator(acc,item):
  print(acc, item)
  return acc+item

print(reduce(accumulator,list2,0))
