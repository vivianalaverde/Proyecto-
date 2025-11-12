import random

print("Bienvenido al juego Piedra Papel o Tijera")
jugador=0
computadora=0

while True:
    eleccion = input("Escribe piedra, papel, tijera o salir: ").lower()
    if eleccion == "salir":
        break
    if eleccion != "piedra" and eleccion != "papel" and eleccion != "tijera":
        print("Opcion invalida. Intenta otra vez.")
        continue

    comp = random.choice(["piedra", "papel", "tijera"])
    print("La computadora eligio:", comp)

    if eleccion == comp:
        print("Empate")
    elif (eleccion == "piedra" and comp == "tijera") or \
         (eleccion == "papel" and comp == "piedra") or \
         (eleccion == "tijera" and comp == "papel"):
        print("GANASTE")
        jugador += 1
    else:
        print("PERDISTE")
        computadora += 1

    print("Puntaje - Tu:", jugador, "| Computadora:", computadora)
    print()

# Resultado final
print("Juego terminado")
print("Puntaje final - Tu:", jugador, "| Computadora:", computadora)
if jugador > computadora:
    print("¡Ganaste el juego!")
elif jugador < computadora:
    print("La computadora gano el juego.")
else:
    print("Empate final.")