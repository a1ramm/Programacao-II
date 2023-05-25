# referência:
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
    
import pygame

pygame.init()

# tamanho da janela
X_SIZE = 1000
Y_SIZE = 600
screen = pygame.display.set_mode((X_SIZE, Y_SIZE))

# pega a referência temporal para poder fazer espera mais à frente
clock = pygame.time.Clock()

# classes :-)
class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sentido_x = 1
        self.sentido_y = 1
        self.velocidade_x = 400
        self.velocidade_y = 400
    def inverte_sentido_x(self):
        self.sentido_x *= -1
        print("virou x em", self.y, "agora é ", self.sentido_x)
    def inverte_sentido_y(self):
        self.sentido_y *= -1
        print("virou y em ", self.x, "agora é ", self.sentido_y)
    def andar(self):
        self.x += self.velocidade_x * self.sentido_x
        self.y += self.velocidade_y * self.sentido_y

class Retangulo(Figura):
    def __init__(self, x, y, x2, y2):
        super().__init__(x, y)
        self.x2 = x2
        self.y2 = y2
        self.color = (255, 0, 0) # cor padrão
    def desenhar(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.x2, self.y2)) 
    def colidiu(self, outro_objeto):    
        area_varredura = pygame.Rect(self.x, self.y, self.x2, self.y2)
        return area_varredura.collidepoint((outro_objeto.x, outro_objeto.y))

class Circulo(Figura):
    def __init__(self, x, y, raio, borda):
        super().__init__(x, y)
        self.raio = raio
        self.borda = borda
    def desenhar(self):
        pygame.draw.circle(screen, (10, 10, 10), [self.x, self.y], self.raio, self.borda)
    def colidiu(self, outro_objeto):    
        area_varredura = pygame.Rect(self.x - self.raio, self.y - self.raio, self.x + self.raio, self.y + self.raio)
        return area_varredura.collidepoint((outro_objeto.x, outro_objeto.y))
       
# definição do quadradão
grandao = Retangulo(20, 40, 50, 50)
grandao2 = Retangulo(150, 150, 120, 120)
grandao3 = Retangulo(400, 300, 120, 120)
grandao4 = Retangulo(650, 450, 120, 120)

vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

grandao.color = vermelho
grandao2.color = verde
grandao3.color = azul
grandao4.color = verde

# definição da bolinha
bolinha = Circulo(5, 300, 15, 5)

def verifica_colisao(quadrado, bola):
    if quadrado.colidiu(bola):
        # verificações: entrou nos domínios de x e y do quadrado?
        dentro_x = (bola.x > quadrado.x) or (bola.x < quadrado.x2)
        dentro_y = (bola.y > quadrado.y) or (bola.y < quadrado.y2)        

        if dentro_x and dentro_y:

            # qual é a maior distância de x entre as bordas?            
            distancia1_x = (bola.x - quadrado.x)
            distancia2_x = (bola.x - quadrado.x2)
            if distancia1_x > distancia2_x:
                maior_x = distancia1_x
            else:
                maior_x = distancia2_x
            
            # qual é a maior distância de y entre as bordas?            
            distancia1_y = (bola.y - quadrado.y)
            distancia2_y = (bola.y - quadrado.y2)
            if distancia1_y > distancia2_y:
                maior_y = distancia1_y
            else:
                maior_y = distancia2_y
            
            # quicou no x ou no y?
            if maior_x > maior_y:
                bola.inverte_sentido_y()
            else:
                bola.inverte_sentido_x()          
    
run = True
while run:

    # código obrigatório para finalizar bem o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    # desenha informações na tela
    screen.fill("purple")    
    grandao.desenhar()
    grandao2.desenhar()
    grandao3.desenhar()
    grandao4.desenhar()
    bolinha.desenhar()

    # desenha os objetos efetivamente
    # o circulo vazou a borda da janela?
    if bolinha.x > X_SIZE or bolinha.x < 0:
       bolinha.inverte_sentido_x()
    if bolinha.y > Y_SIZE or bolinha.y < 0:    
       bolinha.inverte_sentido_y()
    pygame.display.flip()

    # o circulo vazou a borda da janela?
    if bolinha.x > X_SIZE or bolinha.x < 0:
       bolinha.inverte_sentido_x()
    if bolinha.y > Y_SIZE or bolinha.y < 0:    
       bolinha.inverte_sentido_y()
    
    # houve colisão?
    verifica_colisao(grandao, bolinha)
    verifica_colisao(grandao2, bolinha)
    verifica_colisao(grandao3, bolinha)
    verifica_colisao(grandao4, bolinha)
    
    # varia a posição do círculo

    
    # espera um pouco
    clock.tick(60)     

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
        bolinha.x -= 1
        
    if pk[pygame.K_RIGHT]:
        bolinha.x += 1
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
    clock.tick(60)

pygame.quit()
exit()