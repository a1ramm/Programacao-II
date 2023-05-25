# https://www.pygame.org/docs/tut/newbieguide.html

import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

# posições iniciais da bola
x = 320
y = 320
a = 320
b = 320

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit     

    # Do logical updates here.
    # ...

    # captura de eventos do teclado
    pk = pygame.key.get_pressed()
    if pk[pygame.K_LEFT]:
        x -= 1
        
    if pk[pygame.K_RIGHT]:
        x += 1
    if pk[pygame.K_UP]:
        y -= 1
    if pk[pygame.K_DOWN]:
        y += 1
    
    if pk[pygame.K_a]:
        a -= 1
    if pk[pygame.K_d]:
        a += 1
    if pk[pygame.K_w]:
        b -= 1
    if pk[pygame.K_s]:    
        b += 1

    screen.fill("purple")  # Fill the display with a solid color

    pygame.draw.circle(screen, (10, 10, 10), [x, y], 15, 5)
    pygame.draw.circle(screen, (10, 10, 10), [a, b], 15, 5)

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)