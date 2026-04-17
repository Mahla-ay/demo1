import pygame
import random
class Tangerine(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen= screen
        self.surf= pygame.image.load("tangerine.png")
        self.surf2= pygame.transform.scale(self.surf,(35,25))
        self.x= random.randint(0, 700)
        self.y=0
        self.rect= self.surf2.get_rect(topleft=(self.x, self.y))
    def Move(self, event):
        self.y+=5
        self.rect.y= self.y
        self.screen.blit(self.surf2,(self.x, self.y))
        if self.y >= 700:
            self.kill()
        return self.y >= 700

#-----------------------------------------
class Basket(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen= screen
        self.surf= pygame.image.load("Basket.png")
        self.surf2= pygame.transform.scale(self.surf,(80,60))
        self.rect= self.surf2.get_rect()
        self.wb=0
        self.hb=640
        
    def Update(self, W, H):
        mouse_x, mouse_y= pygame.mouse.get_pos()
        min_y= H*2//3
        max_y= H-60
        self.wb= max(0,min(mouse_x, W-80))
        self.hb= max(min_y, min(mouse_y, max_y))
        self.rect.topleft= (self.wb, self.hb)
    def draw(self):
        self.screen.blit(self.surf2,(self.wb,self.hb))
#-------------------------------------------------
class Blueberries(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen= screen
        self.surf= pygame.image.load("Blueberry.png")
        self.surf2= pygame.transform.scale(self.surf,(17,12))
        self.rect= self.surf2.get_rect()
        self.x= random.randint(0, 700)
        self.y=0
        self.rect= self.surf2.get_rect(topleft=(self.x, self.y))
    def Move(self, event):
        self.y+=5
        self.rect.y= self.y
        self.screen.blit(self.surf2,(self.x, self.y))
        if self.y >= 700:
            self.kill()