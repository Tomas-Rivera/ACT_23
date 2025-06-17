from Funciones import *

while True:
    limpiar()
    print("""
    ════════════════════════════════
    ║   ⚜️ MENU CALCULADORAS ⚜️   ║
    ════════════════════════════════  
    ║   1.- Calculador Iva         ║
    ║   2.- Descuento              ║
    ║   3.- Calculador IMC         ║
    ║   0.- Salir                  ║
    ════════════════════════════════ """)
    opcion = int(input("Seleccione una opcion : "))
    match opcion:
        case 0:
            break
        case 1:
            print("Calcular IVA")
            precio = int(input("Ingrese un valor : "))
            calcularIva(precio)
        case 2:
            print("Descuento")
            precio = int(input("Ingrese el valor original : "))
            descuento = float(input("Ingrese su descuento (%) : "))
            DescuentoFuncion(precio, descuento)
        case 3:
            print("Calcular IMC")
            peso = float(input("Ingrese su peso : "))
            altura = float(input("Ingrese su altura : "))
            calcularIMC(peso, altura)
        case _:
            print("❌ Error")