import pygame

# Initialize pygame-ce
pygame.init()

# Window setup
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Pygame CE Test")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw red circle at center
    pygame.draw.circle(screen, RED, (250, 200), 60)

    # Update display
    pygame.display.flip()

# Quit
pygame.quit()
