#Metodos en diccionarios
user ={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}

#user.clear() #Elimina el contenido del diccionario
#user2 = user.copy() #Realiza una copia del diccionario en otra variable
#user.pop('age') #Elimina el valor del parametro de la lista. Devuelve el valor asignado al parametro
user.update({'age':55})# Actualiza un valor dentro del diccionario
user.update({'ages':80})# Si el parametro no esta en el diccionario el metodo lo agrega
print(user)
#print(user2)