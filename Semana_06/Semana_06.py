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


    ejer3()