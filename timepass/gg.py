import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🍎 Fruit Catcher")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 80, 80)
GREEN = (80, 255, 80)
BLUE = (80, 80, 255)

# Basket setup
basket_width, basket_height = 80, 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 40
basket_speed = 8

# Fruit setup
fruit_radius = 15
fruit_x = random.randint(fruit_radius, WIDTH - fruit_radius)
fruit_y = -fruit_radius
fruit_speed = 5

# Game variables
score = 0
font = pygame.font.SysFont("comicsansms", 28)
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    clock.tick(60)
    screen.fill((240, 240, 240))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move fruit
    fruit_y += fruit_speed

    # Check for catching
    if (basket_y < fruit_y + fruit_radius < basket_y + basket_height) and \
       (basket_x < fruit_x < basket_x + basket_width):
        score += 1
        fruit_y = -fruit_radius
        fruit_x = random.randint(fruit_radius, WIDTH - fruit_radius)
        fruit_speed += 0.3  # make it harder

    # Missed fruit
    if fruit_y > HEIGHT:
        score = 0
        fruit_y = -fruit_radius
        fruit_x = random.randint(fruit_radius, WIDTH - fruit_radius)
        fruit_speed = 5

    # Draw basket
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

    # Draw fruit
    pygame.draw.circle(screen, RED, (fruit_x, int(fruit_y)), fruit_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
