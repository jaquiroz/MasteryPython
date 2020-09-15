is_old = True
is_licenced = True
""" 
if is_old:# Por defecto la condicional siempre acepta el valor TRUE
    print("You are old enough to drive!")
elif is_licenced:
    print("You can drive now!")
else:
    print("You are not of age!") """

if is_old and is_licenced:
    print("You are old enough to drive, and you have a licence!")
else:
    print("You are not of age!")

print("ok ok ok")

#==> https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
