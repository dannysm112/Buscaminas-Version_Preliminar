"""
game.py: Contiene la implementación de la clase Game, que controla el flujo del juego Buscaminas.
"""

import pygame
import os
from boton import Button
from tablero import Tablero

class Game():
    def __init__(self):
        """
        Inicializa un objeto Game para controlar el juego Buscaminas.
        """
        self.tablero = None
        self.tamaño = (880, 800)
        self.size = (9, 9)
        self.prob_bomba = 0.14
        self.tamaño_casilla = self.tamaño[0] // self.size[0], self.tamaño[1] // self.size[1]
        self.cargar_imagenes()

    def run(self):
        """
        Inicia la ejecución del juego.
        """
        pygame.init()
        self.menu()

    # Resto del código...
