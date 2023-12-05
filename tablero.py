from casilla import Casilla
from random import random


class Tablero():
    """
    Clase que representa el tablero del juego.

    Atributos:
    - tamaño (tuple): Tupla que indica las dimensiones del tablero (filas, columnas).
    - prob_bomba (float): Probabilidad de que una casilla contenga una bomba.
    - perder (bool): Indica si el jugador ha perdido el juego.
    - ganar (bool): Indica si el jugador ha ganado el juego.
    - num_clicked (int): Número de casillas clicadas por el jugador.
    - num_nobombas (int): Número de casillas sin bomba en el tablero.
    - tablero (list): Lista (bidimensional) que representa el tablero de casillas.

    Métodos:
    - __init__(tamaño, prob_bomba): Inicializa una instancia de Tablero.
    - set_tablero(): Crea el tablero y coloca las bombas según la probabilidad.
    - set_casillas_cercanas(): Asigna las casillas vecinas a cada casilla en el tablero.
    - get_lista_vecinos(index): Retorna la lista de casillas vecinas a la casilla en la posición dada.
    - get_size(): Retorna las dimensiones del tablero.
    - get_casilla(index): Retorna la casilla en la posición dada.
    - handleclick(casilla, bandera): Maneja la interacción del jugador con una casilla.
    - get_perder(): Retorna si el jugador ha perdido el juego.
    - get_ganar(): Retorna si el jugador ha ganado el juego.
    """

    def __init__(self,tamaño, prob_bomba):
        """
        Inicializa una instancia de Tablero.

        Parámetros:
        - tamaño (tuple): Tupla que indica las dimensiones del tablero (filas, columnas).
        - prob_bomba (float): Probabilidad de que una casilla contenga una bomba.
        """
        self.tamaño = tamaño
        self.prob_bomba = prob_bomba 
        self.perder = False
        self.ganar = False 
        self.num_clicked = 0
        self.num_nobombas = 0
        self.set_tablero()


    def set_tablero(self):
        """Crea el tablero y coloca las bombas según la probabilidad dada."""
        self.tablero = []
        for row in range(self.tamaño[0]):
            row = []
            for col in range(self.tamaño[1]):
                bomba = random() < self.prob_bomba
                if (not bomba):
                    self.num_nobombas +=1
                casilla = Casilla(bomba)
                row.append(casilla)
            self.tablero.append(row)
        self.set_casillas_cercanas()

    def set_casillas_cercanas(self):
        """Asigna las casillas vecinas a cada casilla en el tablero."""
        for row in range(self.tamaño[0]):
            for col in range(self.tamaño[1]):
                casilla = self.get_casilla((row,col))
                vecinos = self.get_lista_vecinos((row,col))
                casilla.set_vecinos(vecinos)

    def get_lista_vecinos(self,index):
        """
        Retorna la lista de casillas vecinas a la casilla en la posición dada.

        Parámetros:
        - index (tuple): Posición de la casilla en el tablero.

        Retorna:
        - Lista de casillas vecinas.
        """
        vecinos = []
        for row in range(index[0]-1, index[0]+2):
            for col in range(index[1]-1, index[1]+2):
                fuera_rango = row < 0 or row >= self.tamaño[0] or col < 0 or col >= self.tamaño[1]
                fuera_rango2 = row == index[0] and col == index[1]
                if fuera_rango or fuera_rango2:
                    continue
                vecinos.append(self.get_casilla((row,col)))
        return vecinos

    def get_size(self):
        """Retorna las dimensiones del tablero."""
        return self.tamaño

    def get_casilla(self,index):
        """
        Retorna la casilla en la posición dada.

        Parámetros:
        - index (tuple): Posición de la casilla en el tablero.

        Retorna:
        - Casilla en la posición dada.
        """
        return self.tablero[index[0]][index[1]]

    def handleclick(self,casilla, bandera):
        """
        Maneja la interacción del jugador con una casilla.

        Parámetros:
        - casilla (Casilla): Casilla con la que interactúa el jugador.
        - bandera (bool): Indica si se ha colocado una bandera.

        Efecto:
        - Actualiza el estado del juego según la interacción del jugador.
        """
        if (casilla.get_clicked()) or (not bandera and casilla.get_bandera()):
            return 
        if bandera:
            casilla.toggle_bandera()
            return
        casilla.click()
        if casilla.get_bomba():
            self.perder =  True
            return
        self.num_clicked +=1
        if casilla.get_num_alrededor() != 0:
            return
        for vecino in casilla.get_vecinos():
            if not vecino.get_bomba() and not vecino.get_clicked():
                self.handleclick(vecino,False)

    def get_perder(self):
        """Retorna si el jugador ha perdido el juego."""
        return self.perder

    def get_ganar(self):
        """Retorna si el jugador ha ganado el juego."""
        return self.num_clicked == self.num_nobombas