#!/usr/bin/env python3

# Clase HangmanGame (lógica del juego)
class HangmanGame:

    #Constante para almacenar la cantidad maxima de errores permitidos en el juego.
    MAX_ERRORES = 6

    #Constructor del jueg, recibe palabra secreta
    def __init__(self, palabra_secreta: str):
        #Convertimos la palabra a mayusculas para facilitar comparaciones     
        self.palabra_secreta = palabra_secreta.upper()
        #Inicializacion de errores en 0
        self.errores = 0
        #Inicializacion de conjunto set para letras adivinadas
        self.letras_adivinadas = set()
        #Inicializacion de conjunto set para letras erradas
        self.letras_erradas = set()

    def intentar_letra(self, letra: str):
        letra = letra.upper()
        
        # Si ya la había dicho, no penalizamos
        if letra in self.letras_adivinadas or letra in self.letras_erradas:
            return False, "Ya ingresaste esa letra."

        if letra in self.palabra_secreta:
            self.letras_adivinadas.add(letra)
            return True, "¡Le embocaste!"
        else:
            self.letras_erradas.add(letra)
            self.errores += 1
            return False, "Le erraste, se te viene la noche"

    def ha_perdido(self) -> bool:
        return self.errores >= self.MAX_ERRORES

    def ha_ganado(self) -> bool:
        # Ganó si todas las letras de la palabra fueron adivinadas
        return all(letra in self.letras_adivinadas for letra in self.palabra_secreta if letra.isalpha())

    def obtener_progreso(self) -> str:
        # Devuelve la palabra oculta mostrando solo las letras adivinadas
        return " ".join(letra if (letra in self.letras_adivinadas or not letra.isalpha()) else "_" for letra in self.palabra_secreta)
