#Crea un diccionario que represente productos y cantidades
inventory1={
    "chocolate":3,"biscuits":6,"juice":2,"chips":5
}
#Añade un nuevo elemento y muestralo
inventory1["apples"]=8
print(inventory1)
#Edita el valor de juice para que sea 1
inventory1["juice"]=1
#Elimina el elemento chocolate y muestralo
del inventory1["chocolate"]
print(inventory1)
#Crea un nuevo diccionario
inventory2={"chocolate":6,"biscuits":4,"milk":7,"oranges":3}
#Crea un nuevo diccionario que anide los dos anteriores con las claves branch1 y branch2
inventory={"branch1":inventory1, "branch2":inventory2}
#Muestra el nuevo diccionario
print(inventory)
#Muestra el valor de biscuits en branch2
print(inventory["branch2"]["biscuits"])
#Crea y muestra un nuevo diccionario llamado codes para asignar codigo a los productos de la siguiente lista utilizando la enumeración
products={"cholotate", "biscuits","juice","milk","apples","chips","orange"}
lang_enum=enumerate(products)

codes=dict((i,j)for i,j in lang_enum)
print(codes)