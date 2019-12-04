import pygame as pg


class TextBox:
    def __init__(self, location, rectangle, text, color):
        self.location = location  # what screen to appear on
        self.rectangle = rectangle  # how big to be
        self.text = text  # what to say
        self.color = color  # what color to be
        self.font = pg.font.Font(None, 32)  # what font to be

        # Render the current text.
        self.txt_surface = self.font.render(self.text, True, self.color)

    # sets the input text
    def set_text(self, string):
        self.text = string

    # what to do with every tick
    def update(self):
        # Render the current text.
        self.txt_surface = self.font.render(self.text, True, self.color)
        # Blit the text.
        self.location.blit(self.txt_surface, (self.rectangle.x + 5, self.rectangle.y + 5))
        # Blit the input_box rect.
        pg.draw.rect(self.location, self.color, self.rectangle, 2)


class MutableTextBox(TextBox):
    def __init__(self, location, rectangle, inactive_color, active_color):
        super().__init__(location, rectangle, "", inactive_color)

        self.color_inactive = inactive_color  # what color to be when not selected
        self.color_active = active_color  # what color to be when selected
        self.active = False  # selected or not?

    # do this when clicked
    def clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rectangle.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive

    # do this when enter is pressed
    def returned(self, event):
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    # what to do every tick
    def update(self):
        super().update()
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rectangle.w = width
