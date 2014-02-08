# Diccionarios

D.get(k[, d])	
#Busca el valor de la clave k en el diccionario. Es equivalente a utilizar D[k] pero al utilizar este método podemos indicar un valor a devolver por defecto si no se encuentra la clave, mientras que con la sintaxis D[k], de no existir la clave se lanzaría una excepción.

D.has_key(k)
#Comprueba si el diccionario tiene la clave k. Es equivalente a la sintaxis k in D.

D.items()
#Devuelve una lista de tuplas con pares clave-valor.

D.keys()
#Devuelve una lista de las claves del diccionario.

D.pop(k[, d])
#Borra la clave k del diccionario y devuelve su valor. Si no se encuentra dicha clave se devuelve d si se especificó el parámetro o bien se lanza una excepción.

D.values()
#Devuelve una lista de los valores del diccionario.
