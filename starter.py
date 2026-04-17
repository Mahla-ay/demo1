import pygame
from game_class import * 
pygame.init()
W=730
H=700
screen= pygame.display.set_mode((W,H))
background1= pygame.image.load("starter.jpg")
background2= pygame.image.load("forest.jpg")
pygame.mouse.set_visible(False)
clock= pygame.time.Clock()
tan= Tangerine(screen)
bas= Basket(screen)
berry= Blueberries(screen)
tangerines = []
tangerines_group = pygame.sprite.Group()  
blueberries= []
blueberries_group = pygame.sprite.Group()  
all_sprites = pygame.sprite.Group() 
running= True
start= True
SPAWN_TANGERINE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_TANGERINE, 1500)
score=0
points=2
game_over= False
pygame.mixer.music.load("HP.mp3")
pygame.mixer.music.play(loops=-1)
gameoverSound = pygame.mixer.Sound("GameOver.mp3")
while running:
    clock.tick(30)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start= not start
            if event.type == SPAWN_TANGERINE:
                new_tan = Tangerine(screen)
                tangerines.append(new_tan)
                tangerines_group.add(new_tan)
                new_berry = Blueberries(screen)
                blueberries.append(new_berry)
                blueberries_group.add(new_berry)
            
            
    if start:
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("Press Space To Start", 1, (128, 128, 128))
        background1.blit(text, (350,500))
        font1= pygame.font.SysFont('Papyrus', 40)
        text4 = font1.render("Tangerine Leagues", 1, (255, 140, 0))
        background1.blit(text4,(340,140) )
        screen.blit(background1, (0, 0))
        
        
    else:
        screen.blit(background2, (0, 0))
        for tan in tangerines:
            hit_bottom= tan.Move(None)
            if hit_bottom:
                tangerines.remove(tan)
                tangerines_group.remove(tan)
                points -= 1
                
        for berry in blueberries:
            berry.Move(None)    
        bas.Update(W,H)
        hits= pygame.sprite.spritecollide(bas, tangerines_group, True)
        score += len(hits)
        for hit in hits:
            if hit in tangerines:
                tangerines.remove(hit)
        hit2= pygame.sprite.spritecollide(bas, blueberries_group, True)
        points -= len(hit2)
        if points <= 0:
            game_over = True
            pygame.time.set_timer(SPAWN_TANGERINE, 0)
        for hit in hit2:
            if hit in blueberries:
                blueberries.remove(hit)
        font = pygame.font.SysFont('Arial', 20)
        text2 = font.render(f"Score: {score} ", 1, (255, 255, 255))
        text1 = font.render(f"Points: {points} ", 1, (255, 255, 255))
        screen.blit(text2, (5,5))
        screen.blit(text1, (95,5))
        bas.draw()
        if game_over:
        
            font = pygame.font.SysFont('Arial', 40)
            text = font.render("GAME OVER!", 1, (255, 0, 0))
            textpos = text.get_rect()
            textpos.centerx = screen.get_rect().centerx
            textpos.centery = screen.get_rect().centery
            screen.blit(text, textpos)
            pygame.mixer.music.stop()
            gameoverSound.play(loops=1)
            #running= False
        
        
    pygame.display.flip()


pygame.quit()
