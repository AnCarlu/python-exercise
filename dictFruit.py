#Copia el diccionario a un nuevo diccionario
fruits={1:'apples',2:'bananas',3:'pears',4:'strawberries',5:'watermelons'}
fruits_copy=fruits.copy()
#Muestra una lista de elementos clave-valor de fruits_copy
print(list(fruits_copy.items()))
#Muestra una lista de las claves
print(list(fruits_copy.keys()))
#Muestra una lista de los valores
print(list(fruits_copy.values()))
#Muestra el valor de la clave 3
print(fruits_copy.get(3))
#Actualiza el valor de clave 4
fruits_copy.update({4:'blueberries'})
#Añade un nuevo elemento
fruits_copy.setdefault(6,'pineapples')
#Elimina el elemento con la clave 5
fruits_copy.pop(5)
#Muestra los elementos de la cpia del diccionario
print(list(fruits_copy.items()))
#Eliminar todos los elementos de fruist_copy
fruits_copy.clear()
#Utiliza la siguiente lista de claves para crear un diccionario con el método fromKeys()
Keys=('one','two','three','four')
numbers=dict.fromkeys(Keys)

