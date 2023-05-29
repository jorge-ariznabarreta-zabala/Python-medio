def log(fichero_log): # loguea al archivo que le indicamos
    def decorador_log(func): 
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")
        return decorador_funcion
    return decorador_log

@log('ficherosalida.log')
def suma(a, b):
    return a + b

@log('ficherosalida.log')
def resta(a, b):
    return a - b

@log('ficherosalida.log')
def multiplicadivide(a, b, c):
    return a*b/c

suma(10, 30)
resta(7, 23)
multiplicadivide(5, 10, 2)

# El script que has proporcionado implementa un decorador llamado `log` que se utiliza para registrar las llamadas a ciertas funciones en un archivo de registro especificado. Aquí está el desglose de cómo funciona:

# 1. Se define la función `log` que toma un argumento `fichero_log`, que representa el nombre del archivo de registro al que se desea escribir.

# 2. Dentro de la función `log`, se define otro decorador llamado `decorador_log`. Este decorador toma una función `func` como argumento y se encargará de envolver esa función con la funcionalidad adicional del registro.

# 3. Dentro de `decorador_log`, se define otra función llamada `decorador_funcion`, que actuará como el envoltorio de la función original. Esta función toma cualquier número de argumentos posicionales (`*args`) y argumentos de palabras clave (`**kwargs`).

# 4. Dentro de `decorador_funcion`, se abre el archivo de registro especificado utilizando la declaración `with open(fichero_log, 'a') as opened_file:`. El modo `'a'` se utiliza para abrir el archivo en modo de anexado, lo que significa que los nuevos registros se agregarán al final del archivo.

# 5. A continuación, se invoca la función original `func` con los argumentos proporcionados (`func(*args, **kwargs)`) y se almacena el resultado en la variable `output`.

# 6. Se escribe el resultado en el archivo de registro utilizando `opened_file.write(f"{output}\n")`. Cada registro se agrega como una nueva línea en el archivo de registro.

# 7. Finalmente, se retorna la función `decorador_funcion` como el resultado del decorador `decorador_log`.

# 8. El decorador se utiliza para decorar tres funciones: `suma`, `resta` y `multiplicadivide`. Cada vez que se llama a una de estas funciones, el decorador se activa y registra la llamada y el resultado en el archivo de registro especificado.

# En el ejemplo proporcionado, se invocan las tres funciones `suma`, `resta` y `multiplicadivide` con diferentes conjuntos de argumentos, y sus resultados se registran en el archivo `'ficherosalida.log'`.