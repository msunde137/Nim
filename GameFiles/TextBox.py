import pygame as pg


# creates a simple text object with a bounding box
class TextBox:
    def __init__(self, rectangle, text, color, font, margin=0):
        self.rectangle = rectangle  # how big to be
        self.text = text  # what to say
        self.color = color  # what color to be
        self.font = font  # what font to be
        self.margin = margin  # what the margin should be

        # Render the current text.
        self.txt_surface = self.font.render(self.text, True, self.color)

    # sets the input text
    def set_text(self, string):
        self.text = string

    # what logic to do every tick
    def update(self):
        pass

    # what to render with every tick
    def render(self, location):
        # draws the text with line breaks
        draw_text(location, self.text, self.color, self.rectangle, self.font, self.margin)
        pg.draw.rect(location, self.color, self.rectangle, 2)  # draws the rectangle


# creates an editable text box from TextBox
class MutableTextBox(TextBox):
    def __init__(self, rectangle, inactive_color, active_color, text, font, margin, default_length=10):
        super().__init__(rectangle, text, inactive_color, font, margin)  # call the parent __init__

        self.color_inactive = inactive_color  # what color to be when not selected
        self.color_active = active_color  # what color to be when selected
        self.default_length = default_length  # what the default length is
        self.active = False  # selected or not?
        self.entered = False  # enter key pressed?

    # do this when clicked
    def clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box
            if self.rectangle.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False

    # do this when enter is pressed
    def returned(self, event):
        self.entered = False  # weather enter has been pressed

        # if a key has been pressed
        if event.type == pg.KEYDOWN:
            # if the text box has been selected
            if self.active:
                # if the key pressed was return
                if event.key == pg.K_RETURN:
                    print(self.text)  # print the text to the console
                    self.active = False  # deselect the text box
                    self.entered = True  # set entered to true temporarily
                # otherwise, delete the last character typed
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                # otherwise, add the keycode to the text box
                else:
                    self.text += event.unicode

    # what to do every tick
    def update(self):
        super().update()  # call the parent update
        # Resize the box if the text is too long.
        width = max(self.default_length, self.txt_surface.get_width() + 10)
        self.rectangle.w = width
        print(self.txt_surface.get_width())

    def render(self, location):
        # Change the current color of the input box.
        self.color = self.color_active if self.active else self.color_inactive
        # update the text
        self.txt_surface = self.font.render(self.text, True, self.color)
        # Blit the text.
        location.blit(self.txt_surface, (self.rectangle.x + 5, self.rectangle.y + 5))
        # Blit the input_box rect.
        pg.draw.rect(location, self.color, self.rectangle, 2)


# creates a pushable button from TextBox
class Button(TextBox):
    def __init__(self, rectangle, neutral_color, hover_color, font, margin, text=""):
        super().__init__(rectangle, text, neutral_color, font, margin)  # call the text box __init__
        self.neutral_color = neutral_color  # set neutral color
        self.hover_color = hover_color  # se the hover color

        self.color = neutral_color  # set the current color
        self.pushed = False  # button hasn't been pushed yet
        self.hovered = False  # if mousing over button

    # controls the logic every tick
    def update(self):
        mouse = pg.mouse.get_pos()  # get the mouse position

        # set the color if the mouse is over the box or not
        if self.rectangle.left + self.rectangle.w > mouse[0] > self.rectangle.h and \
                self.rectangle.top + self.rectangle.h > mouse[1] > self.rectangle.top:
            self.color = self.hover_color
            self.hovered = True
        else:
            self.color = self.neutral_color
            self.hovered = False

    # do this if the button has been pushed
    def selected(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rectangle.collidepoint(event.pos):
                # select the button
                self.pushed = True


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def draw_text(surface, text, color, rectangle, font, margin, aa=False, bkg=None):
    rect = rectangle

    y = rect.top
    line_spacing = -2

    # get the height of the font
    font_height = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + font_height - margin > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width - margin and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left + margin, y + margin))
        y += font_height + line_spacing

        # remove the text we just blitted
        text = text[i:]

    return text
