import pygame as pg
from GameFiles import TextBox


def main():
    screen = pg.display.set_mode((400, 300))
    done = False

    text_box = TextBox.TextBox(screen, pg.Rect(50, 50, 50, 32), "Nim", pg.Color("dodgerblue2"))

    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    button = TextBox.Button(screen, input_box, color_inactive, color_active, (0, 0, 0), "Press Me")

    clock = pg.time.Clock()

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            button.selected(event)

        screen.fill((30, 30, 30))

        text_box.update()
        text_box.render()

        button.update()
        button.render()

        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
