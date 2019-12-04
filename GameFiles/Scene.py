import pygame


class BaseScene:
    def __init__(self):
        self.next = self

    def process_input(self, events):
        print("uh-oh, you didn't override this in the child class")

    def update(self):
        print("uh-oh, you didn't override this in the child class")

    def render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def switch_scene(self, next_scene):
        self.next = next_scene


class MenuScene(BaseScene):
    def __init__(self):
        super().__init__()

    # event handler
    def process_input(self, events):
        for event in events:
            # do some things
        pass

    # scene logic here
    def update(self):
        pass

    # render code here
    def render(self, screen):
        pass
