some_list = [ "a","b","c","d","c","e","d"]

dupliacted = list(set([data for data in some_list 
              if some_list.count(data)>1]))
print(dupliacted)
