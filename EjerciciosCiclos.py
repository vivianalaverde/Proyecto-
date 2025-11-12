import random
opcion = -1
while opcion != 0:
    print("\n--- MENU DE EJERCICIOS ---")
    print("1. Sumar impares entre 0 y 30")
    print("2. Sumar 10 numeros ingresados")
    print("3. Contar cuántas veces se escribio 'Juan' ")
    print("4. Juego de apuestas 5 rondas")
    print("5. Analisis de empleados")
    print("0. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        # Ejercicio 1
        i = 1
        suma_impares = 0
        while i < 30:
            suma_impares += i
            i += 2
        print(f"Suma de impares entre 0 y 30: {suma_impares}")

    elif opcion == 2:
        # Ejercicio 2
        contador = 0
        suma_numeros = 0
        while contador < 10:
            num = int(input(f"Ingrese el numero {contador + 1}: "))
            suma_numeros += num
            contador += 1
        print(f"\nSuma total de los numeros ingresados: {suma_numeros}")

    elif opcion == 3:
        # Ejercicio 3
        contador=1
        acumulador=0
        while contador<=10:
            nombre=input("Ingrese su nombre: ").upper()
            if nombre=="JUAN":
                acumulador+=1
            contador+=1
        print("El nombre Juan fue digitado: ",acumulador,"Veces")

    elif opcion == 4:
        # Ejercicio 4
        dinero = float(input("\nIngrese el dinero inicial para apostar: "))
        ronda = 0
        while ronda < 5:
            print(f"\nRonda {ronda + 1}:")
            apuesta = float(input("¿Cuanto desea apostar? "))
            if apuesta > dinero:
                print("No tienes suficiente dinero para esa apuesta.")
                continue
            n1 = random.randint(1, 6)
            n2 = random.randint(1, 6)
            n3 = random.randint(1, 6)
            print(f"Numeros obtenidos: {n1}, {n2}, {n3}")
            if n1 == n2 == n3:
                ganancia = apuesta * 3
                print("¡Triple! Ganaste 3 veces tu apuesta.")
            elif n1 == n2 or n2 == n3 or n1 == n3:
                ganancia = apuesta * 1.5
                print("¡Doble! Ganaste 1.5 veces tu apuesta.")
            else:
                ganancia = -apuesta
                print("No coincidieron. Perdiste tu apuesta.")
            dinero += ganancia
            print(f"Dinero actual: ${dinero:.2f}")
            ronda += 1
        print(f"\n Terminaste el juego con ${dinero:.2f}")

    elif opcion == 5:
        # Ejercicio 5
        N = int(input("\nIngrese el numero de empleados: "))
        contador = 0
        suma_resultante = 0
        gastos_mayores = 0
        while contador < N:
            print(f"\nEmpleado {contador + 1}:")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            salario = float(input("Salario: "))
            gastos = float(input("Gastos mensuales: "))
            salario_neto = salario - gastos
            suma_resultante += salario_neto
            if gastos > salario:
                gastos_mayores += 1
            contador += 1
        print(f"\nSuma total del salario neto: ${suma_resultante:.2f}")
        print(f"Empleados con gastos mayores al salario: {gastos_mayores}")

    elif opcion == 0:
        print("\n¡Gracias por usar el programa! Hasta pronto.")
    else:
        print("Opcion invalida. Intente de nuevo.")