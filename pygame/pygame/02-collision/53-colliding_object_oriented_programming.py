# referência:
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
    
import pygame

pygame.init()

# tamanho da janela
window = pygame.display.set_mode((800, 600))

# pega a referência temporal para poder fazer espera mais à frente
clock = pygame.time.Clock()

# classes :-)
class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sentido = 1
        self.velocidade_x = 3
    def colidiu(self, outro_objeto):
        return outro_objeto.retangulo.collidepoint((self.x, self.y))
    def inverte_sentido(self):
        self.sentido *= -1
    def andar(self):
        self.x += self.velocidade_x * self.sentido

class Retangulo(Figura):
    def __init__(self, x, y, retangulo):
        super().__init__(x, y)
        self.retangulo = retangulo
    def desenhar(self):
        pygame.draw.rect(window, color, self.retangulo) # desenho do retângulo

class Circulo(Figura):
    def desenhar(self):
        pygame.draw.circle(window, (10, 10, 10), [self.x, self.y], 15, 5)
       
# definição do quadradão
rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(100, 100)
grandao = Retangulo(300, 300, rect)

# definição da bolinha
bolinha = Circulo(5, 300)

run = True
while run:

    # código obrigatório para finalizar bem o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # por enquanto o quadradão não pisca mais
    color = (255, 0, 0)

    # desenha informações na tela
    window.fill("purple")    
    grandao.desenhar()
    bolinha.desenhar()

    # desenha os objetos efetivamente
    pygame.display.flip()

    # o circulo vazou a borda da janela?
    if bolinha.x > 800 or bolinha.x < 0 or bolinha.colidiu(grandao):
       bolinha.inverte_sentido()
    
    # varia a posição do círculo
    bolinha.andar()
    
    # espera um pouco
    clock.tick(60)     

pygame.quit()
exit()