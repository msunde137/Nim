import pygame as pg


class Button:
    def __init__(self, location, rectangle, neutral_color, hover_color, select_color, text=""):
        self.location = location
        self.rectangle = rectangle
        self.neutral_color = neutral_color
        self.hover_color = hover_color
        self.select_color = select_color
        self.text = text

        self.color = neutral_color
        self.selected = False

    def update(self):
        mouse = pg.mouse.get_pos()

        if self.rectangle.left + self.rectangle.w > mouse[0] > self.rectangle.l and \
                self.rectangle.top + self.rectangle.h > mouse[1] > self.rectangle.top:
            self.color = self.hover_color
            self.rectangle.inflate(10, 10)
        else:
            self.color = self.neutral_color
            self.rectangle.inflate(-10, -10)

    def draw(self):
        pg.draw.rect(self.location, self.color, self.rectangle, 2)

    def selected(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rectangle.collidepoint(event.pos):
                # select the button
                self.color = self.select_color
                self.selected = True

