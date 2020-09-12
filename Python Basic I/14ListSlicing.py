amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop' #Asignacion de cambio de valor en la lista
new_cart = amazon_cart[:] #Al realizar slice realizamos una copia de la lista original lo cual permite
                          #mutar a la lista
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
