# Ejemplo de excepcion solucionada con bucle
def dividir(num1, num2):
    try: ###
        return num1/num2
    except ZeroDivisionError: ###
        return "Error. No se puede dividir entre 0" ###
while True:
    try: ###
        n1=(int(input("introduce el dividendo: ")))
        n2=(int(input("introduce el divisor: ")))
        break
    except ValueError:  ####
        print ("Vuelve a intentarelo. Introduce solo numeros") ###

print(dividir(n1, n2))

print("Linea de codigo importante")