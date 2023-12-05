class Button():
    """
    Clase que representa un botón en la interfaz gráfica.

    Atributos:
    - image: Superficie de la imagen del botón.
    - x_pos: Posición horizontal del botón.
    - y_pos: Posición vertical del botón.
    - font: Fuente utilizada para el texto del botón.
    - base_color: Color del texto cuando no se pasa el mouse sobre el botón.
    - hovering_color: Color del texto cuando se pasa el mouse sobre el botón.
    - text_input: Texto que se muestra en el botón.
    - text: Superficie de texto utilizando la fuente y el color actual.
    - rect: Rectángulo que delimita el área del botón.
    - text_rect: Rectángulo que delimita el área del texto en el botón.

    Métodos:
    - __init__(image, pos, text_input, font, base_color, hovering_color): Inicializa una instancia de Button.
    - update(screen): Actualiza la representación del botón en la pantalla.
    - checkForInput(position): Verifica si la posición dada está dentro del área del botón.
    - changeColor(position): Cambia el color del texto del botón si el mouse está sobre él.
    """

    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        """
        Inicializa una instancia de Button.

        Parámetros:
        - image: Superficie de la imagen del botón.
        - pos: (x, y) que representa la posición del botón.
        - text_input: Texto que se muestra en el botón.
        - font: Fuente utilizada para el texto del botón.
        - base_color: Color del texto cuando no se pasa el mouse sobre el botón.
        - hovering_color: Color del texto cuando se pasa el mouse sobre el botón.
        """
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        """
        Actualiza la representación visual del botón en la pantalla.

        Parámetros:
        - screen: Superficie de la pantalla donde se representa el botón.
        """
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        """
        Verifica si la posición dada está dentro del área del botón.

        Parámetros:
        - position: (x, y) que representa la posición a verificar.

        Retorna:
        - True si la posición está dentro del área del botón, False de lo contrario.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        """
        Cambia el color del texto del botón si el mouse está sobre él.

        Parámetros:
        - position: (x, y) que representa la posición del mouse.

        Efecto:
        - Actualiza el color del texto del botón según la posición del mouse.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)