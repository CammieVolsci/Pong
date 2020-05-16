import pygame, datetime, random

PLAYER_IMAGE = "assets/paddle.png"
BALL_IMAGE = "assets/ball.png"
WALL_IMAGE = "assets/wall.png"

class Paddle(pygame.sprite.Sprite):

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mover = 0
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.pontuacao = 0
    
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

    random.seed(datetime.time())  

    def __init__(self):
        self.x = random.randint(200,600) 
        self.y = random.randint(250,550) 
        self.mover_x = 7 * pow(-1,random.randint(1,2))
        self.mover_y = 7 * pow(-1,random.randint(1,2))
        self.image = pygame.image.load(BALL_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.ponto1 = False
        self.ponto2 = False

    def desenhar(self,screen):
        screen.blit(self.image,(self.x,self.y))

    def movimento(self):             
        
        self.x += self.mover_x
        self.y += self.mover_y

        if self.x <= 0:
            self.x = 400
            self.y = 325
            self.ponto2 = True
        elif self.x >= 750:
            self.x = 400
            self.y = 325
            self.ponto1 = True

        if self.y <= 0:
            self.mover_y *= -1
        elif self.y >= 600:
            self.mover_y *= -1
        
        self.rect.x = self.x
        self.rect.y = self.y       

class Barrinha:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(WALL_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def desenhar(self,screen):
        screen.blit(self.image,(self.x,self.y))