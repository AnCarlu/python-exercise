#Segun los resultados de la carrera enumera los primeros 3 autos con menos tiempo como ganador de la carrera
#Premia tambien a cada 3ª coche que llegaba a la meta
#Crea dos programas. El primero debe usar sorted() y el segundo sort()

#First program sorted()
car_list=[('Demonio',2367),('Rápido',3798),('Bolt',5612),('Antorcha',3561),('Devil',3578),('Velocidad',4112),('Quemador',3275),('Ritmo',2789),
        ('Roadrunner',4599),('Luz',2563),('Humo',4255),('Parpadeo',3071),('Racer',2050),('Swoosh',4062),('Puntuación',3370),('Snap',5315)]

print("El orden de llegada ha sido")
print(sorted(car_list, key= lambda x:x[1])[:3])

print("El vehiculo que ha llegado cada 3ª posicion")
print(car_list[2::3])

#Second program sort()
#First program sorted()
car_list=[('Demonio',2367),('Rápido',3798),('Bolt',5612),('Antorcha',3561),('Devil',3578),('Velocidad',4112),('Quemador',3275),('Ritmo',2789),
        ('Roadrunner',4599),('Luz',2563),('Humo',4255),('Parpadeo',3071),('Racer',2050),('Swoosh',4062),('Puntuación',3370),('Snap',5315)]

ordered_card_list=car_list.copy()
ordered_card_list.sort(key=lambda x:x[1])
print("Los tres primeros han sido", ordered_card_list[:3])

print("El vehiculo que ha llegado cada 3ª posicion")
print(car_list[2::3])