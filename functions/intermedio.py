lista = [1, 2, 3, 4, 5]
al_cuadrado = list(map(lambda x: x**2, lista))
print(al_cuadrado)

# Como su nombre indica, filter crea una lista de elementos si usados en la llamada a una función devuelven True. Es decir, filtra los elementos de una lista usando un determinado criterio. Veamos un ejemplo:

lista = range(-5, 5)
menor_cero = list(filter(lambda x: x < 0, lista))
print(menor_cero)

from functools import reduce #en python3 reduce se encuentra en modulo functools

nums = [47,11,42,13]
result = reduce(lambda x, y: x + y, nums)
print(result)