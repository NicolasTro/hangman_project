#!/usr/bin/env python3
from player import Player


# Clase HangmanGame (lógica del juego)
class HangmanGame:

    # Constante para almacenar la cantidad maxima de errores permitidos en el juego.
    MAX_ERRORS = 6

    # Constructor del juego, recibe palabra secreta y opcionalmente el jugador
    def __init__(self, word: str, player: Player = None):
        # Variables privadas encapsuladas
        self.__word = word.upper()
        self.__player = player
        self.__max_errors = 6
        self.__errors = 0
        self.__guessed_letters = set()
        self.__letras_erradas = set()

    # Getters / Properties
    @property
    def word(self) -> str:
        return self.__word

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def max_errors(self) -> int:
        return self.__max_errors

    @property
    def errors(self) -> int:
        return self.__errors

    @property
    def guessed_letters(self) -> set:
        return self.__guessed_letters

    @property
    def letras_erradas(self) -> set:
        return self.__letras_erradas
        
    def process_guess(self, letra: str) -> bool:
        
        # Pasamos todo a mayus
        letra = letra.upper()

        # Si la letra se encuentra en la palabra, se agrega a la lista de adivinadas.       
        if letra in self.__word:
            self.__guessed_letters.add(letra)
            return True
        else:
            # Si la letra no se encuentra en la palabra, se agrega a la lista de erradas y se suma un error. 
            self.__letras_erradas.add(letra)
            self.__errors += 1
            return False

    def is_lost(self) -> bool:
        # Comparamos si los errores obtenidos son mayores o iguales al maximo permitido.
        return self.__errors >= self.__max_errors

    def is_won(self) -> bool:
        # Ganó si todas las letras de la palabra fueron adivinadas
        return all(letra in self.__guessed_letters for letra in self.__word if letra.isalpha())

    def display_progress(self) -> str:
        # Devuelve la palabra oculta mostrando solo las letras adivinadas
        return " ".join(letra if (letra in self.__guessed_letters or not letra.isalpha()) else "_" for letra in self.__word)
    def calculate_score(self) -> int:
        # Calcula el puntaje de la partida según las reglas del juego.
        if self.is_won():
            intentos_restantes = self.__max_errors - self.__errors
            return 100 + (intentos_restantes * 10)
        return 0

    def finalize_game(self) -> int:
        # Asigna el puntaje calculado al jugador si existe y lo retorna.
        score = self.calculate_score()
        if self.__player is not None:
            self.__player.puntaje = score
        return score
