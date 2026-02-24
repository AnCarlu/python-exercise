#Representar la tabla en estructuras de datos anindadas
#Parte 1
#Cada fruta tendrá dos colecciones, una para almacenar los años de produccion y otra 
#para almacenar la cantidad de producción, donde:
    #Los años estan en colección ordenada
    #Las cantidades están en recogida ordenada respecto a su año de produccion
frutas={
    'manzanas':[[2019,2020,2021,2022],[342,435,547,419]],
    'naranjas':[[2019,2020,2021,2022],[655,545,714,628]]
}

#Parte 2
#Visualiza los datos de la produccion de naranjas
print(frutas['naranjas'][1])
#Almacena en una variable la produccion máxima de naranjas y concatenalo
max_Orange=max(frutas['naranjas'][1])
print("La producción máxima de naranajas es:",max_Orange,"toneladas")
#Obten el indice de esqa cantidad dentro de la coleccion de cantidades de produccion y muestralo
index_Max=frutas['naranjas'][1].index(max_Orange)
print(index_Max)
#Recupera el año respectivo de la maxima produccion y concatenalo
year_Max=frutas['naranjas'][0][index_Max]
print("El año con máxima producción de naranjas es:",year_Max)

#Parte 3
#En una sola linea muestro el calculo de que año la producion de manzanas estuvo en su minimo
print("El año con producion minima de manzanas es:",frutas['manzanas'][0][frutas['manzanas'][1].index(min(frutas['manzanas'][1]))])