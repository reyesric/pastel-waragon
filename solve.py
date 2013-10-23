import itertools
   
DULCE = 1
FRUTA = 2
CONFITE = 3
MASITA = 4

def matches (a,b,c):
    if a == b == c:
        return True
    if a == b and c == MASITA:
        return True
    if a == c and b == MASITA:
        return True
    if b == c and a == MASITA:
        return True
    
    return False

# la combinacion de ingredientes en el molde se representa como una lista de 9 elementos
#
# A B C
# D E F   --->  A B C D E F G H I
# G H I
#

# Cualquier combinacion exitosa tiene que ser de dos tipos posibles:
# 1) tener 3 elementos de cada tipo
# 2) tener 3 elementos de un tipo, 3 de otro y 2 del tercero, mas una masita
# Armar un prototipo de cada uno de estos escenarios como posibles "fuentes" de las permutaciones

FUENTES = []
FUENTES.append ([DULCE,]*3 + [FRUTA,]*3 + [CONFITE,]*3)
FUENTES.append ([DULCE,]*3 + [FRUTA,]*3 + [CONFITE,]*2 + [MASITA,])
FUENTES.append ([DULCE,]*3 + [FRUTA,]*2 + [CONFITE,]*3 + [MASITA,])
FUENTES.append ([DULCE,]*2 + [FRUTA,]*3 + [CONFITE,]*3 + [MASITA,])

ricas = set()  # bucket de soluciones posibles, remueve duplicados por ser un set
for fuente in FUENTES:   # para cada una de las configurationes iniciales (3+3+2+MASITA)
    for c in set(itertools.permutations (fuente)):   # para cada permutacion removiendo duplicados
        # Si tiene una fila con todos los elementos iguales
        if matches(c[0],c[1],c[2]) or matches(c[3], c[4], c[5]) or matches(c[6], c[7], c[8]):
            ricas.add(c)
        # Si tiene una columna con todos los elementos iguales
        if matches(c[0],c[3],c[6]) or matches(c[1], c[4], c[7]) or matches(c[2], c[5], c[8]):
            ricas.add(c)

print 'Cantidad maxima de pasteles ricos que se pueden hacer:',len(ricas)        

