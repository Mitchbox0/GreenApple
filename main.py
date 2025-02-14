import pygame

pygame.init()

# Set up display
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hollow Knight")

Player = pygame.image.load('images/player.png')
player_x, player_y = 5, 5

# Game loop
running = True
while running:
    screen.fill((30, 30, 30))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                print("Left")  
            if event.key == pygame.K_RIGHT:
                print("Right") 
            if event.key == pygame.K_UP:
                print("Up") 
            if event.key == pygame.K_DOWN:
                print("Down")   

    screen.blit(Player, (player_x, player_y))



    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip()

pygame.quit()
