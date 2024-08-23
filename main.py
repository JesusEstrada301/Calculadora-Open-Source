import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

ficha = 0
print("Menu Calculadora")
print("Suma --> 1")
print("Resta --> 2")
print("Multiplicacion --> 3")
print("Division --> 4")
print("Suma de varios numeros --> 5")
ficha = int(input("Ingrese la opcion deseada: \n"))
if ficha == 1:
    x = int(input("Ingrese el primer numero \n"))
    y = int(input("Ingrese el segundo numero \n"))
    resultado = sumar.suma(x, y)
    print(resultado)
elif ficha == 2:
    x = int(input("Ingrese el primer numero \n"))
    y = int(input("Ingrese el segundo numero \n"))
    resultado = resta.resta(x, y)
    print(resultado)
elif ficha == 3:
    x = int(input("Ingrese el primer numero \n"))
    y = int(input("Ingrese el segundo numero \n"))
    resultado = multiplicacion.multiplicacion(x, y)
    print(resultado)
elif ficha == 4:
    x = int(input("Ingrese el primer numero \n"))
    y = int(input("Ingrese el segundo numero \n"))
    resultado = dividir.dividir(x, y)
    print(resultado)
elif ficha == 5:
    resultado = suma_avanzada.suma_avanzada()
    print(resultado)
else:
    print("Valor ingresado no encontrado.")