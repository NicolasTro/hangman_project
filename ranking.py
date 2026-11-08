#!/usr/bin/env python3
import os
from player import Player


class Ranking:

    def __init__(self, top: int = 10, file_path: str = "ranking.txt"):
        self.__top = top
        self.__file_path = file_path
        self.__players = []
        self.load()

    def add(self, player: Player):
        # Agrega un jugador, ordena de mayor a menor puntaje y conserva el top N
        self.__players.append(player)
        self.__players.sort(key=lambda p: p.puntaje, reverse=True)
        self.__players = self.__players[:self.__top]
        self.save()

    def get_ranking(self):
        # Retorna una copia de la lista de jugadores ordenada.
        return list(self.__players)

    def save(self):
        # Guarda el ranking en el archivo de texto formato: nombre,puntaje
        try:
            with open(self.__file_path, "w", encoding="utf-8") as f:
                for player in self.__players:
                    f.write(f"{player.nombre},{player.puntaje}\n")
        except IOError as e:
            print(f"Error al guardar el ranking: {e}")

    def load(self):
        #Carga el ranking desde el archivo de texto si existe.
        self.__players = []
        if not os.path.exists(self.__file_path):
            return

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and "," in line:
                        parts = line.split(",", 1)
                        name = parts[0].strip()
                        try:
                            score = int(parts[1].strip())
                            if name:
                                self.__players.append(Player(name, score))
                        except ValueError:
                            continue
            # Ordenar y cortar al top N
            self.__players.sort(key=lambda p: p.puntaje, reverse=True)
            self.__players = self.__players[:self.__top]
        except IOError as e:
            print(f"Error al cargar el ranking: {e}")

