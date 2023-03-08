import pygame as pg
from GameFiles import Scene


def run_game(width, height, fps, starting_scene):
    screen = pg.display.set_mode((width, height))  # initialize the screen
    clock = pg.time.Clock()  # initialize the clock
    active_scene = starting_scene  # set the starting scene

    # while there is a scene to run:
    while active_scene is not None:
        pressed_keys = pg.key.get_pressed()  # update the pressed keys

        # Event filtering
        # this only filters the quit events
        # all other events are passed to the scene to be processed
        filtered_events = []
        for event in pg.event.get():
            quit_attempt = False
            if event.type == pg.QUIT:
                quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)  # run any events for the active scene
        active_scene.Update()  # run the update method for the active scene
        active_scene.Render(screen)  # render the active scene

        active_scene = active_scene.next  # update the active scene

        pg.display.flip()  # Update the full display Surface to the screen
        clock.tick(fps)  # set the tick speed


if __name__ == "__main__":
    run_game(400, 300, 60, Scene.TitleScene())
