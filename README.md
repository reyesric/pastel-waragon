pastel-waragon
==============

La combinación de ingredientes en el molde se representa como una lista de 9 elementos, con los elementos de la 1era fila, luego los de la 2da, y al final la 3ra fila

Cualquier combinacion exitosa tiene que ser de dos tipos posibles:
* tener 3 elementos de cada tipo
* tener 3 elementos de un tipo, 3 de otro y 2 del tercero, mas una masita

El programa genera prototipos de cada uno los 2 escenarios y recorre todas las permutaciones de esos escenarios iniciales, removiendo combinaciones duplicadas y guardando las combinaciones que cumplen con la condición de ser "ricas"
