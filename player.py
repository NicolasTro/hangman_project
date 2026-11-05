#!/usr/bin/env python3

class Player:

    def __init__(self, nombre: str, puntaje: int = 0):
        self.nombre = nombre
        self.puntaje = puntaje

#Properties, getNombre()
    @property    
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre = nombre

    @property
    def puntaje(self):
        return self.__puntaje

    @puntaje.setter
    def puntaje(self, puntaje):
        if puntaje < 0:
            raise ValueError("El puntaje no puede ser negativo")
        self.__puntaje = puntaje

    
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Puntaje: {self.__puntaje}"
