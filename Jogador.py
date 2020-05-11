import pygame

PLAYER_IMAGE = "assets/paddle.png"

class Paddle:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mover = 0
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.image.get_rect() 
    
    def desenhar(self,screen):
        screen.blit(self.image,(self.x,self.y))

    def movimento(self):
        self.y += self.mover

        if self.y <= 0:
            self.y = 0
        elif self.y >= 650:
            self.y = 650
        
        self.rect.x = self.x
        self.rect.y = self.y         
