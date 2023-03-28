def S(a, b):
    return a + b
def R(a, b):
    return a - b
def M(a, b):
    return a * b
def D(a, b):
    return a / b

while True:
    print("Menú de Operaciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opc = input("Ingrese una opción: ")
    n1 = float(input("Número 1:"))
    n2 = float(input("Número 2:"))

    if opc=="1":
        print("La suma es: ",S(n1, n2))
    elif opc=="2":
        print("La resta es: ",R(n1, n2))
    elif opc=="3":
        print("La multiplicación es: ",M(n1, n2))
    elif opc=="4":
        print("La división es: ",D(n1, n2))
    else:
        print("Opción Inválida")