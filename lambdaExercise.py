#Escriba una función lambda que acepte un entero como argumento y lo devuleva incrementado en uno
suma=(lambda x: x+1)(5)
print(suma)

#Escriba una función lambda con los parametros name y age y devulevalos en una cadena
cadena=(lambda name, age: f"{name} is {age} years old")(name="Siri",age= 49)
print(cadena)

#Utilice la función map con la función lambda para cambiar los nombres de la lista a mayusculas
fruits=['manzana','naranja','cereza','mango']
uppered_fruits=map(lambda fruit:fruit.upper(), fruits)
print(list(uppered_fruits))