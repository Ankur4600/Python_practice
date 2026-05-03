#we need to find highest even in the list
def highest_even (li):
  tem_li = []
  for value in li:
    if value % 2 != 0:
      tem_li.append(value)
  return max(tem_li)

print(highest_even([2,8,9,6,7,3,5,2,1,21,24,1,44]))