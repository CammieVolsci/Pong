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
        jogadorII = self.jogadorII

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
                elif k == K_s:
                    jogadorI.mover = 8
                if k == K_UP:
                    jogadorII.mover = -8
                elif k == K_DOWN:
                    jogadorII.mover = 8
            elif t == KEYUP:
                if k == K_w or k == K_s:
                    jogadorI.mover = 0
                elif k == K_UP or k== K_DOWN:
                    jogadorII.mover = 0

    def actors_update(self):
        jogadorI = self.jogadorI
        jogadorII = self.jogadorII
        ball = self.ball

        if jogadorI.teste_colisao(ball):
            ball.mover_x *= -1
            jogadorI.pontuacao += 1
        elif jogadorII.teste_colisao(ball):
            ball.mover_x *= -1
            jogadorII.pontuacao += 1
        
        jogadorI.movimento()
        jogadorII.movimento()
        ball.movimento()

    def actors_draw(self):
        jogadorI = self.jogadorI
        jogadorII = self.jogadorII
        ball = self.ball

        jogadorI.desenhar(self.displaysurf)
        jogadorII.desenhar(self.displaysurf)
        ball.desenhar(self.displaysurf)

    def loop(self):        
        self.jogadorI = Jogador.Paddle(10,150)
        self.jogadorII = Jogador.Paddle(750,150)
        self.ball = Jogador.Ball()
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