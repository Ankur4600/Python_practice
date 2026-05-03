#list, set, dictionary

#list comprehensions

my_list =[data for data in "ankur"]
# print(my_list)

my_list2 = [data for data in range(0,99)]
# print(my_list2)

my_list3 = [data*2 for data in range(0,99)]
# print(my_list3)

my_list4 = [data**2 for data in range(0,99) if data %2 == 0]
# print(my_list4)




#set comprehsions

my_set = { data for data in "hello"}
# print(my_set)

my_set2 = {data for data in range(0,99)}
# print(my_set2)

my_set3 = {data ** 2 for data in range(0,99) if data % 2 !=0}
print(my_set3)


#dict comprehsions
simple_dict = {
  "a":2,
  "b":3,
  "c":4
}

my_dict = { key:value**2 for key,value in simple_dict.items()}
print(my_dict)


my_dict2 = { key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
print(my_dict2)

my_dict3 = { num:num**2 for num in [1,2,3,4,5]}
print(my_dict3)