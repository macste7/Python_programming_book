def count(list):
  if list == []:
    return 0
  print (list)
  return 1 + count(list[1:])
  
print (count([1,2,3,4,5,6,7,8]))