pastel-waragon
==============

La combinación de ingredientes en el molde se representa como una lista de 9 elementos

 A B C
 D E F   --->  A B C D E F G H I
 G H I


Cualquier combinacion exitosa tiene que ser de dos tipos posibles:
1) tener 3 elementos de cada tipo
2) tener 3 elementos de un tipo, 3 de otro y 2 del tercero, mas una masita

El programa genera prototipos de cada uno los 2 escenarios y recorre todas las permutaciones de esos escenarios iniciales, removiendo combinaciones duplicadas y guardando las combinaciones que cumplen con la condición de ser "ricas"
