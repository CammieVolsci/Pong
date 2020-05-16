import pygame, Jogador
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (0,0,0)

class PongGame:

    window_width = None
    window_height = None   
    background = None
    displaysurf = None 
    run = True
    fps = None
    game_over = False

    basic_font = None
    small_font = None

    jogadorI = None
    jogadorII = None
    ball = None
    barrinha = []
    
    def __init__(self):
        self.window_width = 800
        self.window_height = 650
        self.fps = 30   
        pygame.init()
        pygame.display.set_caption("Pong")
        self.displaysurf = pygame.display.set_mode((self.window_width,self.window_height))   
        self.basic_font = pygame.font.Font('freesansbold.ttf',32)     
        self.small_font = pygame.font.Font('freesansbold.ttf',20)     

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
                if k == K_r and self.game_over:
                    self.reset()
                if k == K_w and not self.game_over:
                    jogadorI.mover = -10
                elif k == K_s and not self.game_over:
                    jogadorI.mover = 10
                if k == K_UP and not self.game_over:
                    jogadorII.mover = -10
                elif k == K_DOWN and not self.game_over:
                    jogadorII.mover = 10
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
        elif jogadorII.teste_colisao(ball):
            ball.mover_x *= -1
        
        if ball.ponto1 and not self.game_over:
            jogadorI.pontuacao += 1
            ball.ponto1 = False
        elif ball.ponto2 and not self.game_over:
            jogadorII.pontuacao += 1
            ball.ponto2 = False

        jogadorI.movimento()
        jogadorII.movimento()
        ball.movimento()

    def actors_draw(self):
        jogadorI = self.jogadorI
        jogadorII = self.jogadorII
        ball = self.ball
        barrinha = self.barrinha

        jogadorI.desenhar(self.displaysurf)
        jogadorII.desenhar(self.displaysurf)
        ball.desenhar(self.displaysurf)

        for i in range(10):
            barrinha[i].desenhar(self.displaysurf)

    def reset(self):
        self.jogadorI.pontuacao = 0
        self.jogadorII.pontuacao = 0
        self.ball.x = 400
        self.ball.y = 325
        self.game_over = False

    def loop(self):        
        fpsclock = pygame.time.Clock()   
        self.jogadorI = Jogador.Paddle(10,150)
        self.jogadorII = Jogador.Paddle(750,150)
        self.ball = Jogador.Ball()

        for i in range(10):
            self.barrinha.append(Jogador.Barrinha(400,10 + i*100)) 
        
        gameOver1Surf = self.basic_font.render('Game Over | Player 1 Wins',True,BLACK)
        gameOver1Rect = gameOver1Surf.get_rect()
        gameOver1Rect.center = (425, 380)   

        gameOver2Surf = self.basic_font.render('Game Over | Player 2 Wins',True,BLACK)
        gameOver2Rect = gameOver2Surf.get_rect()
        gameOver2Rect.center = (400, 380)   

        resetSurf = self.basic_font.render('Pressione R para reiniciar',True,BLACK)
        resetRect = resetSurf.get_rect()
        resetRect.center = (425, 480)          

        while self.run:    
            pontuacao1_txt = str(self.jogadorI.pontuacao) 
            pontuacao2_txt = str(self.jogadorII.pontuacao)   

            pontuacao1Surf = self.small_font.render('PONTOS: ' + pontuacao1_txt,True,BLACK)
            pontuacao1Rect = pontuacao1Surf.get_rect()
            pontuacao1Rect.center = (90,20)

            pontuacao2Surf = self.small_font.render('PONTOS: ' + pontuacao2_txt,True,BLACK)
            pontuacao2Rect = pontuacao2Surf.get_rect()
            pontuacao2Rect.center = (700,20)   
            
            self.displaysurf.fill(WHITE)      
            self.displaysurf.blit(pontuacao1Surf,pontuacao1Rect) 
            self.displaysurf.blit(pontuacao2Surf,pontuacao2Rect)

            if self.jogadorI.pontuacao >= 10:
                self.displaysurf.blit(gameOver1Surf,gameOver1Rect) 
                self.displaysurf.blit(resetSurf,resetRect)  
                self.game_over = True       
            elif self.jogadorII.pontuacao >= 10:
                self.displaysurf.blit(gameOver2Surf,gameOver2Rect)     
                self.displaysurf.blit(resetSurf,resetRect)  
                self.game_over = True    

            self.handle_events()
            self.actors_update()
            self.actors_draw()           
            
            pygame.display.flip()
            pygame.display.update()  
            fpsclock.tick(self.fps)

def main():
    game = PongGame()
    game.loop()

## MAIN ##
if __name__ == '__main__':
    main()