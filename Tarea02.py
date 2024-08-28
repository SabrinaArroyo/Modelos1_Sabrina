rango1 =range(5,20,2)
print(rango1)

#MUTABILIDAD los rangos no se pueden mutar
rango1 = range(5,20,2)
lista_rango = list(rango1)
print(lista_rango)

# en la posición 5 queda el 100
lista_rango[5]=100
print(lista_rango)

#SUMA -> pasar a lista
rango1 = range(5,20,2)
rango2 = range(2, 15, 3)
lista_sumada = list(rango1) + list(rango2)
print(lista_sumada)

#SCLICING
rango3 = range(20, 100, 2)
print(rango3)
print('aplicando slicing:', rango3[16])

#Convertir tupla -> estaba en lista
print('convirtiendo el rango a tupla:', tuple(rango1))
print('convirtiendo tupla a lista:', list(rango1))
lista1 = list(rango1)
print(lista1)
print('convirtiendo el rango a lista:', list(rango2))
lista2 = list(rango2)
print(lista2)

#FUNCIÓN LEN
print('aplicando la función len:', len(lista1 + lista2))

#Producto por entero otra vez a lista
lista1 = list(rango1)
print(lista1)
list_multiplicada = lista1 * 2
print(list_multiplicada)