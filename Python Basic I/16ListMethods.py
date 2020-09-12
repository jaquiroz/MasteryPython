basket = [1,2,3,4,5]

#ADD
basket.append(100)  #Anade el valor introducido al final de la lista
basket.insert(2,200)#Anade el valor introducido en una posicion de la lista
basket.extend([300])#Anade valores al final de la lista

#print(basket)

#REMOVE
basket1 = [1,2,3,4,5]
#basket1.pop() #Elimina el ultimo valor de la lista. Este metodo devuelve el valor eliminado
#basket1.pop(0) #Elimina el valor correspodiente a la posicion asignada
#basket1.remove(4) #Elimina un valor especifico de la lista
basket1.clear()
print(basket1)

#====>https://www.w3schools.com/python/python_ref_list.asp

#QUEST
basket2 = [1, 2, 3, 4, 5, 4]
print(basket2.index(4))# Realiza una busqueda a lo largo de la lista
print(basket2.count(4))# Realiza un conteo del dato a lo largo de la lista

#=====>https://www.w3schools.com/python/python_ref_keywords.asp

#SORT
basket3 = ['a', 'x', 'b', 'c', 'd', 'e','d']
#basket3.sort()# El metodo no devuelve nada
#print(sorted(basket3)) # La funcion sorted crea una nueva lista
basket3.reverse() # El metodo reverse invierte la lista
print(basket3)
