#!/usr/bin/env python3
import random

def get_random_word():
    """Lee el archivo y devuelve una palabra aleatoria"""
    with open("wordlist.txt", "r", encoding="utf-8") as archivo:
        # Lee todas las líneas, elimina espacios y valida si la lista esta vacía
        palabras = []
        for linea in archivo:
            palabra = linea.strip()
            # Si la línea tiene contenido la agrega a palabras
            if palabra:
                palabras.append(palabra)
    # Valida fuera del ciclo si la lista está vacía
    if not palabras:
        raise ValueError("El archivo wordlist.txt está vacío o no contiene palabras válidas.")
        # Devuelve una palabra al azar de la lista
        return random.choice(palabras)


def draw_hangman(errores: int) -> str:
    """Devuelve el dibujo ASCII  correspondiente a la cantidad de errores (0 a 6)."""
    estados = [
        # 0 errores
        r"""
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        # 1 error: Cabeza
        r"""
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        # 2 errores: Cuerpo
        r"""
          +---+
          |   |
          O   |
          |   |
          |   |
              |
        =========
        """,
        # 3 errores: Brazo izquierdo
        r"""
          +---+
          |   |
          O   |
         /|   |
          |   |
              |
        =========
        """,
        # 4 errores: Ambos brazos
        r"""
          +---+
          |   |
          O   |
         /|\  |
          |   |
              |
        =========
        """,
        # 5 errores: Pierna izquierda
        r"""
          +---+
          |   |
          O   |
         /|\  |
          |   |
         /    |
        =========
        """,
        # 6 errores: Frito
        r"""
          +---+
          |   |
          O   |
         /|\  |
          |   |
         / \  |
        =========
        """
    ]
    indice = min(max(errores, 0), len(estados) - 1)
    return estados[indice]

