import pygame

PLAYER_IMAGE = "assets/paddle.png"
BALL_IMAGE = "assets/ball.png"

class Paddle(pygame.sprite.Sprite):

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mover = 0
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
    
    def desenhar(self,screen):
        screen.blit(self.image,(self.x,self.y))

    def movimento(self):
        self.y += self.mover

        if self.y <= 0:
            self.y = 0
        elif self.y >= 560:
            self.y = 560
        
        self.rect.x = self.x
        self.rect.y = self.y

    def teste_colisao(self,sprite):
        if(self.image!=0):
            return self.rect.colliderect(sprite.rect)            

class Ball:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mover_x = -2
        self.mover_y = 2
        self.direcao = "Esquerda_Baixo"
        self.image = pygame.image.load(BALL_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #x pos e y pos = direita baixo
        #x pos e y neg = direita cima
        #x neg e y pos = esquerda baixo
        #x neg e y neg = esquerda cima

    def desenhar(self,screen):
        screen.blit(self.image,(self.x,self.y))

    def movimento(self):

        if self.direcao == "Esquerda_Cima":
            self.mover_x = -2
            self.mover_y = -2
        elif self.direcao == "Esquerda_Baixo":
            self.mover_x = -2
            self.mover_y = 2
        elif self.direcao == "Direita_Cima":
            self.mover_x = -2
            self.mover_y = 2
        elif self.direcao == "Direita_Baixo":
            self.mover_x = 2
            self.mover_y = 2              
        
        self.x += self.mover_x
        self.y += self.mover_y

        if self.x <= 0:
            if self.direcao == "Esquerda_Cima":
                self.direcao = "Direita_Cima"
            elif self.direcao == "Esquerda_Baixo":
                self.direcao = "Direita_Baixo"
        elif self.x >= 750:
            if self.direcao == "Direita_Cima":
                self.direcao = "Esquerda_Cima"
            elif self.direcao == "Direita_Baixo":
                self.direcao = "Esquerda_Baixo"
        if self.y <= 0:
            if self.direcao == "Esquerda_Cima":
                self.direcao = "Esquerda_Baixo"
            elif self.direcao == "Direita_Cima":
                self.direcao = "Direita_Baixo"
        elif self.y >= 600:
            if self.direcao == "Esquerda_Baixo":
                self.direcao = "Esquerda_Cima"
            elif self.direcao == "Direita_Baixo":
                self.direcao = "Direita_Cima"
        
        self.rect.x = self.x
        self.rect.y = self.y         
