#DICCIONARIOS
diccionario1 = {'llave1': 'guayaba', 'llave2': 'fresa', 'llave3': 'vainilla', 'llave4': 'limón'}
print(diccionario1)

#pop
valor = diccionario1.pop('llave3')
print('valor eliminado', valor)
print('diccionario pop', diccionario1)

#get
valor_llave = diccionario1.get('llave1')
print('valor de la llave1', valor_llave)

#copy
copia_diccionario = diccionario1.copy()
print('copia de diccionario', copia_diccionario)

#keys
claves = diccionario1.keys()
print('claves del diccionario', claves)

#items
items = diccionario1.items()
print('items del diccionario', items)

#fromkeys
nuevas_claves = ['a', 'b', 'c']
nuevo_diccionario = dict.fromkeys(nuevas_claves, 0)
print('nuevo diccionario con claves', nuevo_diccionario)

#popitem
ultimo_elemento = diccionario1.popitem()
print('ultimo elemento del diccionario', ultimo_elemento)

#setdefault
valor_llave6 = diccionario1.setdefault('llave6', 2)
print('valor de la llave6', valor_llave6)

#update
diccionario2 = {'a': 2, 'b': 4, 'c': 6}
diccionario1.update(diccionario2)
print('diccionario actualizado', diccionario1)

#values
valores = diccionario1.values()
print("Valores del diccionario:", valores)

#clear
diccionario1.clear()
print('diccionario vacío', diccionario1)
