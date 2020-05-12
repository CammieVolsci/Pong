import pygame, Jogador
from pygame.locals import *

WHITE = (255,255,255)

class PongGame:

    window_width = None
    window_height = None   
    background = None
    displaysurf = None 
    run = True

    jogadorI = None
    jogadorII = None
    ball = None
    
    def __init__(self):
        self.window_width = 800
        self.window_height = 650
        self.displaysurf = pygame.display.set_mode((self.window_width,self.window_height))        
        pygame.init()
        pygame.display.set_caption("Pong")

    def handle_events(self):
        jogadorI = self.jogadorI

        for event in pygame.event.get():
            t = event.type
            if t in (KEYDOWN,KEYUP):
                k = event.key
            if t == QUIT:
                self.run = False
            elif t == KEYDOWN:
                if k == K_ESCAPE:
                    self.run = False
                if k == K_w:
                    jogadorI.mover = -8
                if k == K_s:
                    jogadorI.mover = 8
            elif t == KEYUP:
                if k == K_w or k == K_s:
                    jogadorI.mover = 0

    def actors_update(self):
        jogadorI = self.jogadorI
        ball = self.ball

        if jogadorI.teste_colisao(ball):
            if ball.direcao == "Esquerda_Cima":
                ball.direcao = "Direita_Cima"
                print("colidiu1")
            elif ball.direcao == "Esquerda_Baixo":
                ball.direcao = "Direita_Baixo"
                print("colidiu2")
            print("colidiu3")
        
        jogadorI.movimento()
        ball.movimento()

    def actors_draw(self):
        jogadorI = self.jogadorI
        ball = self.ball

        jogadorI.desenhar(self.displaysurf)
        ball.desenhar(self.displaysurf)

    def loop(self):        
        self.jogadorI = Jogador.Paddle(10,150)
        self.ball = Jogador.Ball(600,50)
        fpsclock = pygame.time.Clock()
        fps = 30

        while self.run:    
            self.displaysurf.fill(WHITE)       
            self.handle_events()
            self.actors_draw()
            self.actors_update()
            
            pygame.display.flip()
            pygame.display.update()  
            fpsclock.tick(fps)

def main():
    game = PongGame()
    game.loop()

## MAIN ##
if __name__ == '__main__':
    main()