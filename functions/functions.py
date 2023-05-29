# Paso de argumentos a una función.
# Se le puede dar a una función argumentos por defecto al definirla.
def suma(a=0, b=1):  # la función tiene argumentos por defecto
    return a+b


# Diferentes formas de pasar argumentos
x = suma(1, 2)  # por posición
x = suma(b=1, a=2)  # por nombre
x = suma()  # la función tiene argumentos por defecto


def suma(*numeros):  # pasa un iterable sin indice: lo convierte en tupla
    # <class 'tuple'> Da igual si le mandas lista, set o tupla
    print(type(numeros))
    total = 0
    for n in numeros:
        print(n)
        total += n
    return total


tupla1 = (1, 3, 5, 4)  # tupla
print('pasamos una tupla', suma(*tupla1))  # <class 'tuple'>
lista1 = [1, 3, 5, 4]  # lista
print('pasamos una lista', suma(*lista1))  # <class 'tuple'>
set1 = {1, 2, 3, 4}  # set
print('pasamos un set', suma(*set1))  # <class 'tuple'>


def suma(**numeros):
    print(type(numeros))  # <class 'dict'>
    total = 0
    for n in numeros.values():  # numeros.values()
        print(n)
        total += n
    return total


otromas = {"a": 1, "b": 2, "c": 3, "d": 4}
print('pasamos un diccionario', suma(**otromas))
