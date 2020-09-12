#Set
my_set = {1,2,3,4,5} # La estructura de datos solo acepta valores unicos, no acepta valores repetidos
your_set={4,5,6,7,8}

#print(my_set.difference(your_set)) # Diferencia my_set - your_set

#my_set.discard(5) #Descarta el valor de la referencia en el set, pero no devuelve nada
#print(my_set)

#my_set.difference_update(your_set) #Resta 2 sets y modifica a el primero con el residuo
#print(my_set)

#print(my_set.intersection(your_set)) #Devuelve elementos comunes entre 2 sets
#print(my_set & your_set)

#print(my_set.isdisjoint(your_set)) #Devuelve una variable bool=True si 2 sets no tienen elementos en comun

#print(my_set.union(your_set)) #Devuelve la union de 2 sets con elementos no repetidos
#print(my_set | your_set)

print(my_set.issubset(your_set)) #Devuelve una vaiable bool=True si el primer set es subset del segundo
