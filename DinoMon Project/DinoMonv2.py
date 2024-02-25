import pygame
import random

WIDTH = 600
HEIGHT = 600

# Load background image for new game select screen
new_game_background_image = pygame.image.load("new-game-select.png")

# Load health bar images
low_health_image = pygame.image.load("low-health-bar.png")
half_health_image = pygame.image.load("half-health-bar.png")
full_health_image = pygame.image.load("full-health-bar.png")

class Pet:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50
        self.health = 50
        self.feed_timer = 0  # Timer for next feeding
        self.feed_interval = 5  # Time between feedings (in seconds)
        self.hatching_stage = 0  # Stage of egg hatching animation
        self.hatching_timer = 0  # Timer for hatching animation
        self.egg_images = [pygame.image.load(f"egg{i}.png") for i in range(1, 6)]  # Load egg images for animation

    def feed(self):
        if self.feed_timer <= 0:
            self.hunger -= random.randint(5, 15)
            self.happiness += random.randint(1, 5)
            self.health += random.randint(10, 20)  # Increase health by a random amount
            self.feed_timer = self.feed_interval  # Reset the timer

            # Start egg hatching animation
            self.hatching_stage = 1
            self.hatching_timer = 30  # Set the duration of hatching animation

    def update(self):
        self.hunger = max(min(self.hunger, 100), 0)
        self.happiness = max(min(self.happiness, 100), 0)
        self.health = max(min(self.health, 100), 0)
        if self.feed_timer > 0:
            self.feed_timer -= 1
        if self.hatching_timer > 0:
            self.hatching_timer -= 1
            if self.hatching_timer == 0:
                # Finish egg hatching animation
                self.hatching_stage += 1

    def get_egg_image(self):
        if self.hatching_stage == 0:
            return self.egg_images[0]  # Closed egg
        elif self.hatching_stage < 5:
            return self.egg_images[self.hatching_stage]  # Cracking stages
        else:
            return self.egg_images[4]  # Broken egg

    def get_health_bar_image(self):
        if self.health <= 25:
            return low_health_image
        elif self.health <= 50:
            return half_health_image
        else:
            return full_health_image

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Game Select Screen")

clock = pygame.time.Clock()

pet = Pet()

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Simulate feeding action on mouse click
            pet.feed()

    pet.update()

    # Draw new game select screen background
    screen.fill((255, 255, 255))
    screen.blit(new_game_background_image, (0, 0))
    
    # Draw egg for hatching animation
    egg_pos = (WIDTH // 2 - pet.egg_images[0].get_width() // 2, HEIGHT // 2 - pet.egg_images[0].get_height() // 2)
    screen.blit(pet.get_egg_image(), egg_pos)

    # Draw health bar
    health_bar_pos = (WIDTH // 2 - low_health_image.get_width() // 2, HEIGHT - 50)
    screen.blit(pet.get_health_bar_image(), health_bar_pos)

    pygame.display.flip()

pygame.quit()
