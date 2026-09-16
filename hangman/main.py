import pygame 

pygame.init()
screen = pygame.display.set_mode((600, 600 ))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load("./hangman/background_hangman.jpeg")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(bg,(0, 0))
    pygame.draw.circle(bg, (0, 0, 255), 
                 [300,260], 40, 3)
    pygame.draw.line(bg, (0, 0, 255), [300, 500], [300, 300], 5)  
    pygame.draw.line(bg, (0, 0, 255), [300, 400], [200, 300], 5)
    pygame.draw.line(bg, (0, 0, 255), [300, 400], [400, 300], 5)
    pygame.draw.line(bg, (0, 0, 255), [300, 500], [400, 550], 5)
    pygame.draw.line(bg, (0, 0, 255), [300, 500], [200, 550], 5)

    
    pygame.display.flip()

pygame.quit()   
