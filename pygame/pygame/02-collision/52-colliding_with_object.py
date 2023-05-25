# referência:
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame

import pygame

pygame.init()

# tamanho da janela
window = pygame.display.set_mode((800, 600))

# desenha o retângulo que vai perceber a colisão
rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(100, 100)

# posição de uma bola na tela
x = 5
y = 300

# sentido para o qual a bola caminha
sentido = 1

# pega a referência temporal para poder fazer espera mais à frente
clock = pygame.time.Clock()

run = True
while run:

    # código obrigatório para finalizar bem o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # obtém a posição do círculo em forma de ponto
    point = (x, y)

    # verifica se houve colisão
    collide = rect.collidepoint(point)

    # coloca uma cor ou outra, dependendo se houve ou não colisão
    color = (255, 0, 0) if collide else (255, 255, 255)

    # desenha informações na tela
    window.fill("purple")    
    pygame.draw.rect(window, color, rect) # desenho do retângulo
    pygame.draw.circle(window, (10, 10, 10), [x, y], 15, 5) # desenho do círculo
    pygame.display.flip()

    # o circulo vazou a borda da janela?
    if x > 800 or x < 0:
       sentido *= -1 # inverte o sentido 

    # se houve colisão, também inverte o sentido :-)
    if collide:
        sentido*= -1

    # você consegue transformar os dois "ifs" acima em um if só?
    # dica: use o operador OR

    # varia a posição do círculo
    x += 3 * sentido

    # espera um pouco
    clock.tick(60)     

pygame.quit()
exit()