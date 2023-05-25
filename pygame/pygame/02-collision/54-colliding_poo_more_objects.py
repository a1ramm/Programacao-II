# referência:
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
    
import pygame

pygame.init()

# tamanho da janela
X_SIZE = 800
Y_SIZE = 600
window = pygame.display.set_mode((X_SIZE, Y_SIZE))

# pega a referência temporal para poder fazer espera mais à frente
clock = pygame.time.Clock()

# classes :-)
class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sentido_x = 1
        self.sentido_y = 1
        self.velocidade_x = 1
        self.velocidade_y = 1
    def inverte_sentido_x(self):
        self.sentido_x *= -1
    def inverte_sentido_y(self):
        self.sentido_y *= -1
    def andar(self):
        self.x += self.velocidade_x * self.sentido_x
        self.y += self.velocidade_y * self.sentido_y

class Retangulo(Figura):
    def __init__(self, x, y, x2, y2):
        super().__init__(x, y)
        self.x2 = x2
        self.y2 = y2
    def desenhar(self):
        pygame.draw.rect(window, color, (self.x, self.y, self.x2, self.y2)) 
    def colidiu(self, outro_objeto):    
        area_varredura = pygame.Rect(self.x, self.y, self.x2, self.y2)
        return area_varredura.collidepoint((outro_objeto.x, outro_objeto.y))

class Circulo(Figura):
    def __init__(self, x, y, raio, borda):
        super().__init__(x, y)
        self.raio = raio
        self.borda = borda
    def desenhar(self):
        pygame.draw.circle(window, (10, 10, 10), [self.x, self.y], self.raio, self.borda)
    def colidiu(self, outro_objeto):    
        area_varredura = pygame.Rect(self.x - self.raio, self.y - self.raio, self.x + self.raio, self.y + self.raio)
        return area_varredura.collidepoint((outro_objeto.x, outro_objeto.y))
       
# definição do quadradão
grandao = Retangulo(200, 100, 220, 210)

# definição da bolinha
bolinha = Circulo(5, 300, 15, 5)

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
    if bolinha.x > X_SIZE or bolinha.x < 0:
       bolinha.inverte_sentido_x()
    if bolinha.y > Y_SIZE or bolinha.y < 0:    
       bolinha.inverte_sentido_y()
    
    # houve colisão?
    if grandao.colidiu(bolinha):
        # quicou em x?
        if (bolinha.x > grandao.x) or (bolinha.x < grandao.x2):
            bolinha.inverte_sentido_x()
        else:
            #(bolinha.y > grandao.y) or (bolinha.y < grandao.y2):
            bolinha.inverte_sentido_y()      
    
    # varia a posição do círculo
    bolinha.andar()
    
    # espera um pouco
    clock.tick(60)     

pygame.quit()
exit()