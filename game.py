import pygame
import os
from boton import Button
from tablero import Tablero

class Game():
    """
    Clase principal que gestiona el juego.

    Atributos:
    - tablero (Tablero): Representa el tablero del juego.
    - tamaño (tuple): Dimensiones de la ventana del juego.
    - size (tuple): Dimensiones del tablero.
    - prob_bomba (float): Probabilidad de que una casilla contenga una bomba.
    - tamaño_casilla (tuple): Tamaño de cada casilla en píxeles.
    - screen (pygame.Surface): Superficie de la ventana del juego.
    - images (dict): Diccionario que relaciona nombres de imágenes a superficies.
    """
    
    def __init__(self):
        """
        Inicializa una instancia de Game.

        Atributos:
        - tablero (None): El tablero se inicializa luego con la función Tablero().
        - tamaño (tuple): Dimensiones de la ventana del juego.
        - size (tuple): Dimensiones del tablero.
        - prob_bomba (float): Probabilidad de que una casilla contenga una bomba.
        - tamaño_casilla (tuple): Tamaño de cada casilla en píxeles.
        - screen (None): La superficie de la ventana se inicializa luego con la función actualizar_display().
        - images (dict): Diccionario que relaciona nombres de imágenes a superficies.
        """
        self.tablero = None
        self.tamaño =  (880,800)
        self.size = (9,9)
        self.prob_bomba = 0.14 
        self.tamaño_casilla =  self.tamaño[0] // self.size[0], self.tamaño[1] // self.size[1]
        self.cargar_imagenes()

    def run(self):
        """
        Inicia el juego de buscaminas.

        Inicializa Pygame, muestra el menú principal y maneja los eventos del juego.
        """
        pygame.init()
        self.menu()

    def menu(self):
        """
        Muestra el menú principal del juego.

        Permite al jugador elegir entre jugar, ajustar opciones o salir del juego.
        """
        self.actualizar_display("Buscaminas")
        while True:
            menu_posicion = pygame.mouse.get_pos()
            menu_texto = self.get_font(75).render("Buscaminas", True, "#b68f40")
            MENU_RECT = menu_texto.get_rect(center=(400, 200))
            boton_play = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 350), text_input="JUGAR", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            boton_opciones = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 525),text_input="OPCIONES", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            boton_salir = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 700), text_input="QUIT", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            self.screen.blit(menu_texto, MENU_RECT)

            for button in [boton_play, boton_opciones, boton_salir]:
                button.changeColor(menu_posicion)
                button.update(self.screen)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_play.checkForInput(menu_posicion):
                        pass
                        self.tablero = Tablero(self.size, self.prob_bomba)
                        self.actualizar_display_juego()
                        self.play()
                    if boton_opciones.checkForInput(menu_posicion):
                        pass
                        self.opciones()
                    if boton_salir.checkForInput(menu_posicion):
                        pygame.quit()
            pygame.display.update()

    def opciones(self):
        """
        Muestra la pantalla de opciones.

        Permite al jugador elegir entre niveles de dificultad y volver al menú principal.
        """
        self.actualizar_display("Opciones")

        while True:
            opciones_pos = pygame.mouse.get_pos()
            opciones_texto = self.get_font(75).render("Opciones", True, "#b68f40")
            MENU_RECT = opciones_texto.get_rect(center=(400, 100))
            boton_facil = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), text_input="FACIL", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            boton_medio = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 400),text_input="MEDIO", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            boton_dificil = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 550), text_input="DIFICIL", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            boton_exit = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 700), text_input="ATRAS", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            self.screen.blit(opciones_texto, MENU_RECT)

            for button in [boton_facil, boton_medio, boton_dificil, boton_exit]:
                button.changeColor(opciones_pos)
                button.update(self.screen)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_facil.checkForInput(opciones_pos):
                        pass
                        self.size = (9,9)
                        self.prob_bomba = 0.14
                    if boton_medio.checkForInput(opciones_pos):
                        pass
                        self.size = (10,10)
                        self.prob_bomba = 0.17
                    if boton_dificil.checkForInput(opciones_pos):
                        pass
                        self.size = (12,12)
                        self.prob_bomba = 0.2
                    if boton_exit.checkForInput(opciones_pos):
                        self.menu()
            pygame.display.update()

    def play(self):
        """
        Inicia el juego.

        Gestiona los eventos del juego mientras mientras se está jugando, muestra el tablero y termina el juego si es necesario.
        """
        running =  True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False 
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    posicion = pygame.mouse.get_pos()
                    right_click = pygame.mouse.get_pressed()[2]
                    self.handleclick(posicion,right_click)
            self.mostrar()
            pygame.display.flip()
            if self.tablero.get_ganar():
                running= False
                mensaje = "GANADO"
            if self.tablero.get_perder():
                running = False
                mensaje = "PERDIDO"
        self.juego_terminado(mensaje)

    def juego_terminado(self, mensaje):
        """
        Muestra la pantalla de juego terminado.

        Permite al jugador volver a jugar o salir del juego.
        """
        self.actualizar_display("HA " + mensaje)

        while True:
            opciones_pos = pygame.mouse.get_pos()
            opciones_texto = self.get_font(75).render("HA "+mensaje, True, "#b68f40")
            MENU_RECT = opciones_texto.get_rect(center=(400, 100))
            boton_volver = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 400), text_input="VOLVER A JUGAR", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            boton_salir = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 600), text_input="QUIT", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            self.screen.blit(opciones_texto, MENU_RECT)

            for button in [boton_volver, boton_salir]:
                button.changeColor(opciones_pos)
                button.update(self.screen)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_volver.checkForInput(opciones_pos):
                        pass
                        self.menu()
                    if boton_salir.checkForInput(opciones_pos):
                        pass
                        pygame.quit()
            pygame.display.update()

    def mostrar(self):
        """
        Muestra el tablero en la ventana del juego.
        """
        top_left = (0,0)
        for row in range(self.tablero.get_size()[0]):
            for col in range(self.tablero.get_size()[1]):
                casilla = self.tablero.get_casilla((row,col)) 
                imagen = self.get_imagen(casilla)
                self.screen.blit(imagen,top_left)
                top_left = top_left[0] + self.tamaño_casilla[0], top_left[1]
            top_left = 0, top_left[1]  + self.tamaño_casilla[1]

    def handleclick(self,posicion,right_click):
        """
        Maneja el clic del mouse en una casilla del tablero.

        Parámetros:
        - posicion (tuple): Posición del clic del mouse.
        - right_click (bool): Indica si el clic fue con el botón derecho.

        Actualiza el estado del tablero según la interacción del jugador.
        """
        if (self.tablero.get_perder()):
            return
        index = posicion[1] //self.tamaño_casilla[1] , posicion[0] // self.tamaño_casilla[0]
        casilla = self.tablero.get_casilla(index)
        self.tablero.handleclick(casilla,right_click)

    def get_font(self,tamaño):
        """
        Retorna una fuente de Pygame con el tamaño dado.

        Parámetros:
        - tamaño (int): Tamaño de la fuente.

        Retorna:
        - pygame.font.Font: Objeto de fuente de Pygame.
        """
        return pygame.font.Font("assets/font.ttf",tamaño)
    
    def cargar_imagenes(self):
        """
        Carga las imágenes necesarias para el juego.

        Las imágenes se escalan al tamaño de las casillas del tablero.
        """
        self.images = {}
        for filename in os.listdir("images"):
            if (not filename.endswith(".png")): 
                continue
            imagen = pygame.image.load(r"images/" + filename)
            imagen = pygame.transform.scale(imagen, self.tamaño_casilla)
            self.images[filename.split(".")[0]] = imagen

    def get_imagen(self,casilla):
        """
        Retorna la imagen correspondiente a una casilla.

        Parámetros:
        - casilla (Casilla): Casilla del tablero.

        Retorna:
        - pygame.Surface: Superficie de la imagen.
        """
        string = None
        if casilla.get_clicked():
            string = "bomb-at-clicked-block" if casilla.get_bomba() else str(casilla.get_num_alrededor())
        else:
            string = "flag" if casilla.get_bandera() else "empty-block"
        return self.images[string]

    def actualizar_display(self, mensaje):
        """
        Actualiza la superficie de la ventana del juego.

        Parámetros:
        - mensaje (str): Texto que se muestra en la barra de título.
        """
        self.screen = pygame.display.set_mode(self.tamaño)
        pygame.display.set_caption(mensaje)

    def actualizar_display_juego(self):
        """
        Actualiza la superficie de la ventana del juego según las dimensiones del tablero.
        """
        self.tamaño_casilla =  self.tamaño[0] // self.tablero.get_size()[1], self.tamaño[1] // self.tablero.get_size()[0]
        self.cargar_imagenes()