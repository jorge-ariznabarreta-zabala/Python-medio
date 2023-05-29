import crear #importa todo el modulo
print ("importa todo el modulo. crear.create()=> ", crear.create())
#utiliza nombre_modulo.funcion_o variable...

import crear as patata #importa todo el modulo con nombre patata
print ("importa todo el modulo con nombre patata. patata.create()=> ",patata.create())
#utiliza patata.funcion_o variable...

from crear import create as nuevo, read as mira, read_all as trae_todo, patch as update, delete as papelera
#importa sólo las funciones que necesitas, dandoles nombres
print(nuevo(), '\n', mira(), '\n', trae_todo(), '\n', update(), '\n', papelera(), '\n')
#se utiliza con el nuevo nombre