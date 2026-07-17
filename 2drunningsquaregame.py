import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Endless Runner")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 50, 50)

lanes = [100, 300, 500]
current_lane = 1 

player = pygame.Rect(0, HEIGHT - 150, 60, 60)
player.centerx = lanes[current_lane]

obstacles = []
obstacle_speed = 7
spawn_timer = 0

score = 0
font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if event.pos[0] < WIDTH / 2 and current_lane > 0:
                current_lane -= 1
            elif event.pos[0] > WIDTH / 2 and current_lane < 2:
                current_lane += 1
            player.centerx = lanes[current_lane]
            
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            game_over = False
            obstacles.clear()
            score = 0
            obstacle_speed = 7
            current_lane = 1
            player.centerx = lanes[current_lane]

    if not game_over:
        spawn_timer += 1
        if spawn_timer > 30: 
            lane_choice = random.choice(lanes)
            new_obstacle = pygame.Rect(0, -100, 60, 60)
            new_obstacle.centerx = lane_choice
            obstacles.append(new_obstacle)
            spawn_timer = 0
            score += 1
            
            if score % 10 == 0:
                obstacle_speed += 1

        for obs in obstacles[:]:
            obs.y += obstacle_speed
            if obs.top > HEIGHT:
                obstacles.remove(obs)
            if player.colliderect(obs):
                game_over = True

    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, (200, 0), (200, HEIGHT), 2)
    pygame.draw.line(screen, WHITE, (400, 0), (400, HEIGHT), 2)

    if not game_over:
        pygame.draw.rect(screen, BLUE, player)
        for obs in obstacles:
            pygame.draw.rect(screen, RED, obs)
        
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
    else:
        game_over_text = font.render("GAME OVER - Tap to Restart", True, RED)
        text_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(game_over_text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
