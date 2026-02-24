#1. Escriba una función generadora que imprima el número con la multiplicación de 2 al ranfo dado de enteros
def generate_num(number):
    for i in range(number):
        yield i
#LLame a la función con el argumento 5 y almacene el objeto en una variable
result=generate_num(5)
#Imprime cada valor en pantalla
for value in result:
    print(value)

#2.Escriba una función generadora que devuleva dos cadenas
def multi_yields():
    str1="Python World!"
    yield str1
    str2="Funciones avanzadas del generador en Python"
    yield str2
#LLame a la fucnión y almacene el objeto de retorno dentro de una variable iterable
itr_obj=multi_yields()
#Imprima cada rendimiento con el método next()
print(next(itr_obj))
print(next(itr_obj))