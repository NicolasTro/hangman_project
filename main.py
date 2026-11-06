#!/usr/bin/env python3
from game import HangmanGame
import utils

# Obtenemos una palabra secreta y se la pasamos a Game
palabra_secreta = utils.get_palabra_random()
juego = HangmanGame(palabra_secreta)

print("~~Juego del ahorcado~~")

# El juego continúa hasta que gane o pierda
while not juego.ha_ganado() and not juego.ha_perdido():
    print(utils.dibujar_ahorcado(juego.errores))
    print(f"Palabra: {juego.obtener_progreso()}")
    print(f"Errores: {juego.errores}/{juego.MAX_ERRORES}")

    if juego.letras_erradas:
        print(f"Letras erradas: {', '.join(sorted(juego.letras_erradas))}")

    # Valida la entrada
    entrada_valida = False
    entrada = ""
      
    while not entrada_valida:
        # Solicita al jugador que ingrese una letra
        entrada = input("\nIngresa una letra: ").strip().upper()

        # Valida que sea una sola letra y que pertenezca al alfabeto
        if len(entrada) != 1 or not entrada.isalpha():
            print("Error: Ingresa una sola letra válida.")
        else:
            entrada_valida = True
              
    exito, mensaje = juego.intentar_letra(entrada)
    print(f"\n{mensaje}")

# Fin del juego
print(dibujar_ahorcado(juego.errores))
print("========================= GAMEOVER =========================")
    
if juego.ha_ganado():
    print(f"¡Felicitaciones! Ganaste. La palabra era: {juego.palabra_secreta}")
else:
    print(f"¡Perdiste! Se te vino la noche. La palabra era: {juego.palabra_secreta}

        
