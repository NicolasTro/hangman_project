#!/usr/bin/env python3
import sys
from game import HangmanGame
from player import Player
from ranking import Ranking
import utils

# Inicializamos el gestor de ranking
ranking = Ranking()

print("")
print("~~ Juego del Ahorcado ~~")

# Pedir y validar nombre del jugador al inicio
nombre_valido = False
jugador = None
while not nombre_valido:
    nombre_input = input("Ingresa tu nombre: ").strip()
    try:
        jugador = Player(nombre_input)
        nombre_valido = True
    except ValueError as e:
        print(f"Error: {e}. Intenta nuevamente.")

# Obtenemos una palabra secreta y creamos la partida asociando al jugador
palabra_secreta = utils.get_random_word()
juego = HangmanGame(palabra_secreta, jugador)

# El juego continúa hasta que gane o pierda
while not juego.is_won() and not juego.is_lost():
    print(utils.draw_hangman(juego.errors))
    print(f"Palabra: {juego.display_progress()}")
    # Tarea 5: Mostrar intentos restantes como max_errors - errors
    intentos_restantes = juego.max_errors - juego.errors
    print("")
    print(f"Intentos restantes: {intentos_restantes}")

    if juego.letras_erradas:
        print(f"Letras erradas: {', '.join(sorted(juego.letras_erradas))}")

    # Tarea 3: Valida la entrada (longitud 1, letra válida y no repetida)
    entrada_valida = False
    entrada = ""
      
    while not entrada_valida:
        # Solicita al jugador que ingrese una letra o el 5 para salir
        entrada = input("\nIngresa una letra (o '5' para salir): ").strip().upper()

        if entrada == "5":
            print(f"\n¡Juego cancelado! Gracias por jugar, {jugador.nombre}.")
            sys.exit(0)

        # Valida que sea una sola letra y que pertenezca al alfabeto
        if len(entrada) != 1 or not entrada.isalpha():
            print("Error: Ingresa una sola letra válida o '5' para salir.")
        elif entrada in juego.guessed_letters or entrada in juego.letras_erradas:
            print(f"Error: La letra '{entrada}' ya fue intentada.")
        else:
            entrada_valida = True
              
    # Tarea 4: process_guess retorna booleano
    acerto = juego.process_guess(entrada)
    if acerto:
        print(f"\n¡Le embocaste con '{entrada}'!")
    else:
        print(f"\nLe erraste con '{entrada}', se te viene la noche.")

# Fin del juego: HangmanGame calcula y asigna el puntaje al jugador
puntos = juego.finalize_game()

print(utils.draw_hangman(juego.errors))
print("========================= GAMEOVER =========================")
    
if juego.is_won():
    print(f"\n¡Felicitaciones {jugador.nombre}! Ganaste. La palabra era: {juego.word}")
    print(f"Puntaje obtenido: {puntos} pts")
else:
    print(f"\n¡Perdiste {jugador.nombre}! Se te vino la noche. La palabra era: {juego.word}")
    print("Puntaje obtenido: 0 pts")

# Registrar y guardar en el ranking
ranking.add(jugador)

# Mostrar el Top 10 del ranking
print("\n========== TABLA DE POSICIONES (TOP 10) ==========")
top_jugadores = ranking.get_ranking()
for posicion, p in enumerate(top_jugadores, start=1):
    print(f"{posicion}. {p.nombre} - {p.puntaje} pts")
print("===================================================\n")
