import pygame
import sys
import random

pygame.init()

# Pydroid 3 will usually scale this window to fit your phone screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mobile Coin Collector")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

player = pygame.Rect(400, 300, 50, 50)
coin = pygame.Rect(200, 200, 30, 30)

score = 0
font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

running = True
while running:
    # --- INPUT ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # MOBILE CONTROLS: Listen for finger taps or drags
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            # event.pos gives the exact (X, Y) coordinates of your finger
            player.centerx = event.pos[0]
            player.centery = event.pos[1]

    # --- UPDATE ---
    # Keep player on the screen
    if player.left < 0: player.left = 0
    if player.right > WIDTH: player.right = WIDTH
    if player.top < 0: player.top = 0
    if player.bottom > HEIGHT: player.bottom = HEIGHT

    # Check if the player touches the coin
    if player.colliderect(coin):
        score += 1
        coin.x = random.randint(0, WIDTH - coin.width)
        coin.y = random.randint(0, HEIGHT - coin.height)

    # --- RENDER ---
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, GREEN, coin)
    pygame.draw.rect(screen, RED, player)
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
