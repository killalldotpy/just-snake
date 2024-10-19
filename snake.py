import pygame
import sys
import random

# Initiera Pygame
pygame.init()

# Skärmstorlek
width = 600
height = 400

# Färger
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Skapa spelområdet
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake-spel')

# Klocka för att kontrollera hastigheten
clock = pygame.time.Clock()

# Ormens startposition
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Matens position
food_pos = [random.randrange(1, (width // 10)) * 10,
            random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Rörelseriktning
direction = 'RIGHT'
change_to = direction

# Poäng
score = 0

# Funktion för att visa poäng
def show_score():
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render('Poäng: ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width / 10, 15)
    screen.blit(score_surface, score_rect)

# Spelloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Kontrollera tangenttryckningar
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                if direction != 'DOWN':
                    direction = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                if direction != 'UP':
                    direction = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if direction != 'RIGHT':
                    direction = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if direction != 'LEFT':
                    direction = 'RIGHT'

    # Flytta ormen
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Väx ormen
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width // 10)) * 10,
                    random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    # Bakgrund
    screen.fill(black)

    # Rita ormen
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    # Rita maten
    pygame.draw.rect(screen, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Kontrollera om ormen träffar väggarna eller sig själv
    if snake_pos[0] < 0 or snake_pos[0] > width - 10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > height - 10:
        game_over = True
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over = True

    if 'game_over' in locals() and game_over:
        font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = font.render(
            'Game Over', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (width / 2, height / 4)
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # Visa poäng
    show_score()

    # Uppdatera skärmen
    pygame.display.update()

    # Ställ in hastigheten
    clock.tick(15)