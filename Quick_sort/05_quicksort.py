def quicksort(array):
  if len(array) < 2:
    # przypadek bazowy, tablice puste i z jednym elementem s� ju� posortowane
    return array
  else:
    # przypadek rekurencyjny
    pivot = array[0]
    # podtablica zawieraj�ca wszystkie elementy mniejsze od �rodkowego
    less = [i for i in array[1:] if i <= pivot]
    # podtablica zawieraj�ca wszystkie elementy wi�ksze od �rodkowego
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([10, 5, 2, 3])