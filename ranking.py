#!/usr/bin/env python3

class Ranking:
    
    def __init__(self, top: int = 10, archivo: str = "ranking.txt"):
        
        self.__top = top
        self.__archivo = archivo
        self.__lista = []

   

        