from os import system
from msvcrt import getch
def limpiar():
    print("Presione una tecla para continuar")
    getch()
    system("cls")

def calcularIMC(peso, altura):
    imc = peso/(altura**2)
    print(f"Su IMC es : {imc} ")
    if imc<=18.5:
        print("Bajo peso")
    elif imc>=18.5 and imc<=24.9:
        print("Peso Adecuado")
    elif imc>=25.0 and imc<=29.9:
        print("Sobrepeso")
    elif imc>=30.0 and imc<=34.9:
        print("Obesidad Grado 1")
    elif imc>=35.0 and imc<=39.9:
        print("Obesidad grado 2")
    elif imc>=40:
        print("Obesidad grado 3")                
    return



def calcularIva(precio):
    iva = round(precio*0.19)
    print(f"Su iva es de : {iva} ")
    return iva



def DescuentoFuncion(precio, descuento):
    total = round(precio*(descuento/100))
    print(f"Su total con descuento es de : {total}")
    return

