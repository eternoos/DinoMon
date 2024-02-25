import pygame
import random

WIDTH = 600
HEIGHT = 600

# Load background image for new game select screen
new_game_background_image = pygame.image.load("new-game-background.png")

# Load health bar images
low_health_image = pygame.image.load("low-health-bar.png")
half_health_image = pygame.image.load("half-health-bar.png")
full_health_image = pygame.image.load("full-health-bar.png")

# Load egg cracking images
egg_images = [pygame.image.load(f"egg{i}.png") for i in range(1, 6)]
egg_index = 0

# Load baby dinosaur image
baby_dino_image = pygame.image.load("baby-dinosaur.png")
baby_dino_image = pygame.transform.scale(baby_dino_image, (300, 300))  # Resize baby dinosaur image

# Timer variables
feed_timer = 0
feed_interval = 5
health = 100
baby_hatched = False
crack_egg = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Game")

# Draw new game select screen background
screen.fill((255, 255, 255))
screen.blit(new_game_background_image, (0, 0))

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not baby_hatched and not crack_egg:
                crack_egg = True
                egg_index += 1
            elif event.key == pygame.K_r:  # Reset the game
                egg_index = 0
                baby_hatched = False
                crack_egg = False
                feed_timer = 0
                health = 100
                screen.fill((255, 255, 255))
                screen.blit(new_game_background_image, (0, 0))

    # Update feed timer
    if not baby_hatched:
        feed_timer += 1

    # Update health bar
    if not baby_hatched and feed_timer >= feed_interval:
        health -= random.randint(1, 5)  # Decrease health after a certain period of time
        feed_timer = 0


    # Draw health bar near egg
    health_bar_pos = (WIDTH // 2 - full_health_image.get_width() // 2, HEIGHT // 2 + 150)
    screen.blit(full_health_image, health_bar_pos)

    # Draw egg or baby dinosaur
    if not baby_hatched:
        if crack_egg and egg_index < len(egg_images):
            screen.fill((255, 255, 255))
            screen.blit(new_game_background_image, (0, 0))
            egg_image = egg_images[egg_index]
            egg_pos = (WIDTH // 2 - egg_image.get_width() // 2, HEIGHT // 2 - egg_image.get_height() // 2)
            screen.blit(egg_image, egg_pos)
            crack_egg = False
        elif egg_index >= len(egg_images):
            screen.fill((255, 255, 255))
            screen.blit(new_game_background_image, (0, 0))
            screen.blit(baby_dino_image, (WIDTH // 2 - baby_dino_image.get_width() // 2, HEIGHT // 2 - baby_dino_image.get_height() // 2))
            baby_hatched = True

    pygame.display.flip()

pygame.quit()
