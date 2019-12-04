import pygame
import TextBox


def main():
    screen = pygame.display.set_mode((400, 300))
    done = False

    text_box = TextBox.TextBox(screen, pygame.Rect(50, 50, 50, 32), "Nim", pygame.Color("dodgerblue2"))

    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    input_text_box = TextBox.MutableTextBox(screen, input_box, color_inactive, color_active)

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            input_text_box.clicked(event)
            input_text_box.returned(event)

        screen.fill((30, 30, 30))

        text_box.update()
        input_text_box.update()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
