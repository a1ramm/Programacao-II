# referência:
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame

import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

# desenha o retângulo que vai perceber a colisão
rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(100, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # obtém a posição do mouse
    point = pygame.mouse.get_pos()

    # verifica se houve colisão
    collide = rect.collidepoint(point)

    # coloca uma cor ou outra, dependendo se houve ou não colisão
    color = (255, 0, 0) if collide else (255, 255, 255)

    # desenha informações na tela
    window.fill(0)
    pygame.draw.rect(window, color, rect)
    pygame.display.flip()

pygame.quit()
exit()