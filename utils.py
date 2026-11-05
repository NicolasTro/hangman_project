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
