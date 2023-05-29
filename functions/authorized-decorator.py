autenticado = True
#autenticado = False

def requiere_autenticación(f):
    def funcion_decorada(*args, **kwargs):
        if not autenticado:
            print("Error. El usuario no se ha autenticado")
        else:
            return f(*args, **kwargs)
    return funcion_decorada

@requiere_autenticación
def di_hola():
    print("Hola")
    
di_hola()

# En este script, se define una función decoradora llamada `requiere_autenticación` que se utiliza para verificar si el usuario está autenticado antes de ejecutar una función decorada. Aquí está el desglose de cómo funciona:

# 1. Se define una variable `autenticado` y se le asigna el valor `True`. Esta variable representa el estado de autenticación del usuario.

# 2. Se define la función `requiere_autenticación`, que toma una función `f` como argumento y actuará como el decorador.

# 3. Dentro de `requiere_autenticación`, se define otra función llamada `funcion_decorada`, que actúa como el envoltorio de la función original. Esta función toma cualquier número de argumentos posicionales (`*args`) y argumentos de palabras clave (`**kwargs`).

# 4. Dentro de `funcion_decorada`, se verifica si la variable `autenticado` es `False`, lo que indica que el usuario no está autenticado. En ese caso, se imprime un mensaje de error diciendo que el usuario no se ha autenticado.

# 5. Si la variable `autenticado` es `True`, lo que indica que el usuario está autenticado, se invoca la función original `f` con los argumentos proporcionados (`f(*args, **kwargs)`).

# 6. Finalmente, la función `funcion_decorada` se devuelve como resultado del decorador `requiere_autenticación`.

# 7. El decorador se utiliza para decorar la función `di_hola`. Esto se logra usando la sintaxis `@requiere_autenticación` justo encima de la definición de la función. Esto significa que cada vez que se llama a `di_hola()`, el decorador `requiere_autenticación` se activa y verifica si el usuario está autenticado antes de ejecutar la función `di_hola()`.

# En el ejemplo proporcionado, se invoca la función `di_hola()`. Antes de ejecutarla, el decorador `requiere_autenticación` verifica el estado de autenticación del usuario. Si el usuario está autenticado (es decir, `autenticado` es `True`), se ejecuta la función `di_hola()` y se imprime "Hola". Sin embargo, si el usuario no está autenticado (es decir, `autenticado` es `False`), se imprime un mensaje de error indicando que el usuario no se ha autenticado.