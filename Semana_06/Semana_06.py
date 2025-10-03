def ejer1():
    valor = int(input("Ingrese el número de la tabla: "))

    i = 1

    while valor <=0:
        valor = int(input("Error. Ingrese el número de la tabla: "))

    print()
    while i<=12:
        print(f"{valor} = {i}")
        i+=1

def ejer2():
    sp = si = 0 ;
    while True:
        num = int(input("Ingrese número (0 salir): "))
        if num <0:
            print("Error. No se permite negativos!")
            continue

        if num == 0:
            break

        if num% 2 ==0:
            sp+= num
        else:
            si += num #si = si+num (es el mismo)

    print("/nSuma de pares: ",sp)
    print("Suma de impares: ",si)
    print("/nGracias por utilizar el sistema. Presione enter para salir")

def ejer3():
     f = int(input("Ingrese la cantidad de filas: "))
     c = int(input("Ingrese la cantidad de columnas: "))

     print()

     i = 0
     while i <= f:
         j = 0
         while j <= c:
             print("*", end=" ")
             j+=1
         print()
         i+=1

def ejer4():
    g = input("Genere una contraseña: ")

    print("____________________________________")
    print("       VALIDA TU CONTRASEÑA")
    print("                                    ")
    print("     1. Ud. Tiene 3 intentos        ")
    print("____________________________________")

    intento = 3

    while intento > 0:
         c = input("Ingrese su contraseña: ")

         if g == c:
             print("Acceso concedido: Bienvenido.")
             break
         else:
             intento -= 1
             print(f"Contraseña incorrecta. Tienes {intento} intentos")
    else: print("\nCerrando programa. Usted no puede acceder al sistema")


ejer4()
        