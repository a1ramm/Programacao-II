# https://www.pygame.org/docs/tut/newbieguide.html

import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color


    # desenha um círculo
    # https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    # circle(surface, color, center, radius, width)
    # superfície, cor, centro, raio, borda
    pygame.draw.circle(screen, (10, 10, 10), [320, 320], 15, 5)
    pygame.draw.circle(screen, (15, 15, 15), [325, 325], 20, 10)
    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)

