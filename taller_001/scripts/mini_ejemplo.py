# Definimos una lista
mi_lista = [1, 7, 2, 'a', 8, 'b']

# Imprimimos por pantalla la lista
print('Esta es mi lista {0}'.format(mi_lista))

# Imprimimos el primer y el segundo elemento de la lista
print('Primer elemento de la lista')
print(mi_lista[0])	# Recordamos que el indice para contar empieza en 0.

print('Segundo elemento de la lista')
print(mi_lista[1])


# Definimos un diccionario
listado_edades = {'Maria' : 15, 'Juan': 14, 'Pedro': 19}

# Imprimimos por pantalla los identificadores o keys del diccionario
print('Identificadores del diccionario')
print(listado_edades.keys())

# Imprimimos por pantalla los valores o values del diccionario
print('Valores del diccionario')
print(listado_edades.values())

# Imprimimos por pantalla los conjuntos key, value del diccionario.
print('Identificadores y Valores del diccionario')
print(listado_edades.items())



# Un bucle y la importancia de la indentacion en python
print('Trabajamos con un bucle que recorre mi_lista')
print(mi_lista)

for key in [1, 2, 3, 7]:
   print(key)
   print('me encuentro dentro del bucle')


print('estoy fuera del bucle')
