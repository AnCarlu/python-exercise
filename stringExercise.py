str1= 'El código incorrecto se puede limpiar. Pero es muy caro.'
str2= 'Sé el cambio que deseas ver en el mundo.'
str3= 'El gran secreto de la vide es que no hay secreto.'
con_str= str1+str2+str3
print(con_str)
ext_str=con_str[9:20]
print(ext_str)
print(ext_str.replace('e','a'))
print('secreto' in con_str)
print(ext_str.lower())
print(con_str.split('.'))
con_str.replace('/','.')
print(con_str.join())