class Casilla():
    """
    Clase que representa una casilla en el juego.

    Atributos:
    - bomba (bool): Indica si la casilla contiene una bomba.
    - clicked (bool): Indica si la casilla ha sido seleccionada por el jugador.
    - bandera (bool): Indica si se ha colocado una bandera en la casilla.
    - vecinos (list): Lista de casillas vecinas a la actual.
    - num_alrededor (int): Número de bombas alrededor de la casilla.

    Métodos:
    - get_bomba(): Retorna el valor del atributo 'bomba'.
    - get_clicked(): Retorna el valor del atributo 'clicked'.
    - get_bandera(): Retorna el valor del atributo 'bandera'.
    - set_vecinos(vecinos): Establece la lista de casillas vecinas y actualiza 'num_alrededor'.
    - set_num_alrededor(): Calcula el número de bombas alrededor de la casilla.
    - get_num_alrededor(): Retorna el valor del atributo 'num_alrededor'.
    - toggle_bandera(): Cambia el estado del atributo 'bandera'.
    - click(): Marca la casilla como seleccionada por el jugador.
    - get_vecinos(): Retorna la lista de casillas vecinas.
    """
    
    def __init__(self,bomba):
        """
        Inicializa una instancia de Casilla.

        Parámetros:
        - bomba (bool): Indica si la casilla contiene una bomba.
        """
        self.bomba = bomba
        self.clicked = False
        self.bandera = False

    def get_bomba(self):
        """Retorna el valor del atributo 'bomba'."""
        return self.bomba

    def get_clicked(self):
        """Retorna el valor del atributo 'clicked'."""
        return self.clicked 

    def get_bandera(self):
        """Retorna el valor del atributo 'bandera'."""
        return self.bandera

    def set_vecinos(self,vecinos):
        """
        Establece la lista de casillas vecinas y actualiza 'num_alrededor'.

        Parámetros:
        - vecinos (list): Lista de casillas vecinas.
        """
        self.vecinos = vecinos
        self.set_num_alrededor()

    def set_num_alrededor(self):
        """Calcula el número de bombas alrededor de la casilla."""
        self.num_alrededor = 0
        for casilla in self.vecinos:
            if casilla.get_bomba():
                self.num_alrededor +=1


    def get_num_alrededor(self):
        """Retorna el valor del atributo 'num_alrededor'."""
        return self.num_alrededor

    def toggle_bandera(self):
        """Cambia el estado del atributo 'bandera'."""
        self.bandera = not self.bandera

    def click(self):
        """Marca la casilla como seleccionada por el jugador."""
        self.clicked=True

    def get_vecinos(self):
        """Retorna la lista de casillas vecinas."""
        return self.vecinos