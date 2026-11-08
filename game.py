#!/usr/bin/env python3
from player import Player


# Clase HangmanGame (lógica del juego)
class HangmanGame:

    # Constante para almacenar la cantidad maxima de errores permitidos en el juego.
    MAX_ERRORS = 6

    # Constructor del juego, recibe palabra secreta y opcionalmente el jugador
    def __init__(self, word: str, player: Player = None):
        # Convertimos la palabra a mayusculas para facilitar comparaciones     
        self.word = word.upper()
        self.player = player
        # Tarea 2: Atributos oficiales
        self.max_errors = 6
        self.errors = 0
        # Inicializacion de conjunto set para letras adivinadas y erradas
        self.guessed_letters = set()
        self.letras_erradas = set()
        
    def display_progress(self) -> str:
        # Muestra la palabra oculta
        progreso = []
        for char in self.word:
            if not char.isalpha() or char in self.guessed_letters:
                progreso.append(char)
            else:
                progreso.append("_")
        return " ".join(progreso)

    def process_guess(self, letra: str) -> bool:
        
        # Pasamos todo a mayus
        letra = letra.upper()

        # Si la letra se encuentra en la palabra, se agrega a la lista de adivinadas.       
        if letra in self.word:
            self.guessed_letters.add(letra)
            return True
        else:
            # Si la letra no se encuentra en la palabra, se agrega a la lista de erradas y se suma un error. 
            self.letras_erradas.add(letra)
            self.errors += 1
            return False

    def is_lost(self) -> bool:
        # Comparamos si los errores obtenidos son mayores o iguales al maximo permitido.
        return self.errors >= self.max_errors

    def is_won(self) -> bool:
        # Ganó si todas las letras de la palabra fueron adivinadas
        return all(letra in self.guessed_letters for letra in self.word)

    def calculate_score(self) -> int:
        # Calcula el puntaje de la partida según las reglas del juego.
        if self.is_won():
            intentos_restantes = self.max_errors - self.errors
            return 100 + (intentos_restantes * 10)
        return 0

    def finalize_game(self) -> int:
        # Asigna el puntaje calculado al jugador si existe y lo retorna.
        score = self.calculate_score()
        if self.player is not None:
            self.player.puntaje = score
        return score
