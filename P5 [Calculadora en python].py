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
            n2 = float(input("Ingresa el primer numero: "))
