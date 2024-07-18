#importación de librerias 
import sumar
import resta
import multiplicacion
import division
import suma_avanzada
from suma_avanzada import suma_avanzada
#Muestra al usuario las opciones disponibles para realizar cálculos.
def menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N números")
    print("0. Salir")
    #Convierte la entrada del usuario en un número entero utilizando:
    opcion = int(input("Ingrese una opción: "))
    return opcion

#bucle while que llame repetidamente a la función menu().
while True:
    opcion = menu()

    if opcion == 0:
        break
    elif opcion == 1:
        # Suma
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar.sumar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == 2:
        # Resta
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = resta.resta(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == 3:
        # Multiplicación
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicacion.multiplicacion(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == 4:
        # División
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        while num2 == 0:
            print("No se puede dividir entre cero. Ingrese otro número.")
            num2 = float(input("Ingrese el segundo número: "))
        resultado = division.division(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == 5:
    # Suma avanzada
        numeros = []  # inicializa la lista llamada números
        while True:
            num = float(input("Ingrese un número (0 para terminar): ")) #En cada iteración del bucle, se le pide al usuario que ingrese un número. El valor ingresado se convierte a un número de punto flotante (con decimales) y se almacena en la variable num.
            if num == 0:
                break
            numeros.append(num)
        resultado = suma_avanzada(*numeros)  # El operador * desempaqueta la lista numeros, pasando cada elemento individualmente como argumento a la función.
        print("El resultado de la suma es:", resultado)
else:
    print("Opción invalida. Por favor ingrese una opción valida.")