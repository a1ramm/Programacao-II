# https://www.pygame.org/docs/tut/newbieguide.html

import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

# posições iniciais da bola
x = 320
y = 320

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    # captura de eventos do teclado
    # https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
    pk = pygame.key.get_pressed()
    if pk[pygame.K_UP]:
        y -= 1
    if pk[pygame.K_DOWN]:
        y += 1

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    pygame.draw.circle(screen, (10, 10, 10), [x, y], 15, 5)

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)

