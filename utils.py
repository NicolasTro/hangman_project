#!/usr/bin/env python3
import random

def get_random_word():
    """Lee el archivo y devuelve una palabra aleatoria"""
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        
        # Lee todas las líneas, elimina espacios y filtra las palabras válidas
        words = []
        for line in file:
            word = line.strip()
            if word.isalpha():
                words.append(word)
                
        # Selecciona y devuelve una palabra al azar de la lista filtrada
        return random.choice(words)


def dibujar_ahorcado(errores: int) -> str:
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

