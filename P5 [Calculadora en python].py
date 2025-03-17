def calculadora():
    print("BIENVENIDO A LA CALCULADORA EN PYTHON ;D\n")
    print("Selecciona la operacion que deseas realizar:")
    print("1.Suma")
    print("1.Resta")
    print("1.Muoltiplicacion")
    print("1.Division")

    while True:
        opt = input("Ingresa el numero de la operacion (1/2/3/4): ")
        try:
            n1 = float(input("Ingresa el primer numero: "))
            n2 = float(input("Ingresa el segundo numero: "))
            except ValueError:
                print("Entrada invalida, ingrese un numero valido.")
                continue
            if opt == '1':
                print(f"La suma de los numeros es: {n1 + n2}")
            if opt == '2':
                print(f"La resta de los numeros es: {n1 - n2}")
            if opt == '3':
                print(f"La multiplicacion de los numeros es: {n1 * n2}")
            if opt == '4':
                print(f"La division de los numeros es: {n1 / n2}")
