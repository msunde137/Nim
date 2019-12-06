import pygame as pg
from GameFiles import TextBox as tb
from GameFiles import GameBoards as gb


class SceneBase:
    def __init__(self):
        self.next = self  # what the next scene should be
        self.color_active = pg.Color('dodgerblue2')  # active color for all text boxes
        self.color_inactive = pg.Color('lightskyblue3')  # inactive color for all text boxes

        pg.init()  # initialize the pygame libraries?

    # this is where the events are handled
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    # this is where the scene logic is handled
    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    # this is where the rendering is handled
    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    # switches to a new scene
    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)


# this is the first scene that is loaded
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)  # call the base scene __init__

        margin = 7  # set the text margin

        title_font = pg.font.SysFont("timesnewroman", 30)  # initialize the title font

        # initialize the title box
        self.title_box = tb.Button(pg.Rect(100, 25, 200, 50), self.color_inactive, self.color_inactive, title_font,
                                   margin, "        Nim")

        readme_font = pg.font.SysFont("timesnewroman", 15)  # set the font fro the readme
        readme_text = "In hac habitasse platea dictumst. Mauris pretium porttitor" \
                      " diam vel placerat. Integer eget diam leo. Quisque feugiat" \
                      " augue elit. Sed auctor pulvinar dictum."

        # initialize the explanation box
        # this is where we can put an overview of the project
        self.explanation_box = tb.TextBox(pg.Rect(200, 125, 150, 140), readme_text, self.color_inactive, readme_font,
                                          margin)

        game_font = pg.font.SysFont("timesnewroman", 25)  # initialize the button font
        self.boxes = {
            "listButton": tb.Button(pg.Rect(50, 125, 100, 40), self.color_inactive, self.color_active, game_font,
                                    margin, "List"),
            "stackButton": tb.Button(pg.Rect(50, 175, 100, 40), self.color_inactive, self.color_active, game_font,
                                     margin, "Stack"),
            "queButton": tb.Button(pg.Rect(50, 225, 100, 40), self.color_inactive, self.color_active, game_font,
                                   margin, "Que"),
        }

    # this is where the events for the scene are handled
    def ProcessInput(self, events, pressed_keys):
        # for each event, check if it is relevant
        for event in events:
            if event.type == pg.KEYDOWN and pg.key == pg.K_ESCAPE:
                self.SwitchToScene(TitleScene())
            for button in self.boxes:
                self.boxes[button].selected(event)

    # this is where all the scene logic is handled
    def Update(self):
        # for each button, update it
        for button in self.boxes:
            self.boxes[button].update()

        self.title_box.update()

        # the following code handles which button does what
        if self.boxes["listButton"].pushed:
            self.SwitchToScene(NimScene())
        elif self.boxes["queButton"].pushed:
            self.SwitchToScene(QueScene())
        elif self.boxes["stackButton"].pushed:
            self.SwitchToScene(StackScene())
        pass

        if self.title_box.hovered:
            self.title_box.set_text("     Big Nim")
        else:
            self.title_box.set_text("        Nim")

    # this handles the graphics for the scene
    def Render(self, screen):
        screen.fill((50, 50, 50))  # fill the background grey

        # for each buton, render it
        for button in self.boxes:
            self.boxes[button].render(screen)

        self.explanation_box.render(screen)  # render the explanation box
        self.title_box.render(screen)  # render the title box


# this is the classic nim scene
class NimScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)  # call the base __init__ first

        starting_board = [3, 5, 7]  # the starting board for the game
        self.game_board = gb.ListBoard(starting_board)  # initialize the game board

        font = pg.font.SysFont("timesnewroman", 26)  # initialize the font
        margin = 7  # the margin for text boxes

        self.turn = 0  # whose turn it is
        self.turn_indicator_text = ["Player 0", "Player 1"]  # text indicating whose turn it is
        self.colors = [(200, 0, 0), (0, 0, 200)]  # color indicating whose turn it is

        # initialize the turn indicator text box
        self.turn_indicator = tb.TextBox(pg.Rect(125, 25, 150, 40), self.turn_indicator_text[self.turn],
                                         self.colors[self.turn], font, margin)

        # initialize the game board text boxes
        # these will be how the player plays nim
        self.text_boxes = {
            0: tb.MutableTextBox(pg.Rect(100, 100, 50, 32), self.color_active, self.color_inactive,
                                 str(starting_board[0]), font, margin),
            1: tb.MutableTextBox(pg.Rect(175, 100, 50, 32), self.color_active, self.color_inactive,
                                 str(starting_board[1]), font, margin),
            2: tb.MutableTextBox(pg.Rect(250, 100, 50, 32), self.color_active, self.color_inactive,
                                 str(starting_board[2]), font, margin),
        }

        rules_font = pg.font.SysFont("timesnewroman", 16)  # initialize the rules font
        rules_text = "This is classic nim. Each player takes turns lowering the number in one of the boxes. The goal " \
                     "is to force your opponent to change the last box to 0. Click on a box to enter the new value," \
                     "and press enter to pass the turn."

        # initialize the rules text box
        # this will explain how to play
        self.rules_box = tb.TextBox(pg.Rect(75, 150, 250, 125), rules_text, self.color_inactive, rules_font, margin)

    # this method handles all the one time events in the scene
    def ProcessInput(self, events, pressed_keys):
        # for each event check if they actually happened in the scene
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.SwitchToScene(TitleScene())
            # for each text box, call the event functions for it
            for box in self.text_boxes:
                current_box = self.text_boxes[box]  # which box to look at

                current_box.clicked(event)  # see if the box has been clicked
                current_box.returned(event)  # see if the box is being typed in

                # attempt the following steps and if they error, ignore the error
                try:
                    box_item = int(current_box.text)  # define the current string as an int

                    # if the current int is less than the corresponding int in the game_board,
                    # change the one in the game board
                    if self.game_board.board[box] > int(box_item) and current_box.entered:
                        self.game_board.set_item(box, int(box_item))
                        current_box.text = str(self.game_board.board[box])  # resets the text if it is less than 0

                        # change the turn variable
                        if self.turn == 0:
                            self.turn = 1
                        else:
                            self.turn = 0
                except Exception:
                    pass
        pass

    # this handles the frame to frame logic of the scene
    def Update(self):
        # for each text box
        for box in self.text_boxes:
            current_box = self.text_boxes[box]  # define the current box

            # make sure the length of the text doesn't exceed 2
            if len(current_box.text) > 2:
                current_box.text = current_box.text[:-1]  # if it does, reduce it

            if not current_box.active:
                current_box.text = str(self.game_board.board[box])

        self.turn_indicator.update()  # update the turn indicator text box

        # if the game board is in a winning state
        if self.game_board.check_win_state():
            self.turn_indicator.text = self.turn_indicator_text[self.turn] + "Wins!"  # change the turn indicator text
            pg.time.delay(2000)  # delay for 2 seconds
            self.SwitchToScene(TitleScene())  # switch back to the menu scene
        pass

    def Render(self, screen):
        screen.fill((50, 50, 50))  # fill the background grey

        # for each text box, render the text box
        for box in self.text_boxes:
            self.text_boxes[box].render(screen)

        self.turn_indicator.color = self.colors[self.turn]  # update the turn indicator color
        self.turn_indicator.text = self.turn_indicator_text[self.turn]  # update the turn indicator text
        self.turn_indicator.render(screen)  # render the turn indicator
        self.rules_box.render(screen)  # render the rules text box


class StackScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.SwitchToScene(TitleScene())
        pass

    def Update(self):
        pass

    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((50, 50, 50))


class QueScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.SwitchToScene(TitleScene())
        pass

    def Update(self):
        pass

    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))
