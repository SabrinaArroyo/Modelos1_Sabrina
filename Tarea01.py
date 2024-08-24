bailes = ['ballet', 'contemporaneo', 'jazz', 'tap', 'salsa','flamenco', 'belly dance' ]
#añadir 1 item al final de la lista
bailes.append('bachata')
print(bailes)

#añadir varios items
bailes.extend( ['hula', 'tango', 'merengue'])
print(bailes)

#insertar un item en una posición
bailes.insert(2,'disco')
print(bailes)

#remover el primer item
bailes.remove('tap')
print(bailes)

#remover item último lugar
bailes.pop()
print(bailes)

#quitar todos los items
bailes.clear()
print(bailes)

#encontrar un elemento
bailes = ['ballet', 'contemporaneo', 'jazz', 'tap', 'salsa','flamenco', 'belly dance' ]
bailes.index('ballet')
print(bailes)

#cuantas veces sale un elemento
print(bailes.count('contemporaneo'))

#ordenar lista alfabética
bailes.sort()
print(bailes)

#elementos al revés
bailes.reverse()
print(bailes)

#copia de lista
bailes = ['ballet', 'contemporaneo', 'jazz', 'tap', 'salsa','flamenco', 'belly dance' ]
bailes_2 = bailes.copy()
print(bailes)

