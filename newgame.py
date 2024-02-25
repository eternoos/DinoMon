import pygame
import DinoMonv2
import sys

WIDTH = 600
HEIGHT = 600

def load_image(image_path):
    return pygame.image.load(image_path)

def draw(screen, image):
    screen.blit(image, (0, 0))
    pygame.display.flip()

def new_game():
    # Your new game initialization logic here
    print("Starting a new game...")

def quit_game():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("New Game Screen")
    clock = pygame.time.Clock()

    new_game_screen = load_image("game-new.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 140 <= event.pos[0] <= 260 and 160 <= event.pos[1] <= 200:
                    new_game()
                elif 140 <= event.pos[0] <= 260 and 220 <= event.pos[1] <= 260:
                    quit_game()

        draw(screen, new_game_screen)
        clock.tick(30)

if __name__ == "__main__":
    main()
