def sum(list):
  if list == []:
    return 0
  print (list) #jak widać po lewej wartości zapisują się w częściowo wykonanych wywołań funkcji
  return list[0] + sum(list[1:])
print (sum([1,2,3,4]))