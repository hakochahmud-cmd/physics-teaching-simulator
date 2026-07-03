import pygame
from config import WIDTH, HEIGHT, FPS, TITLE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 30))  # Dark retro background
    
    # Title
    title_text = pygame.font.SysFont("consolas", 48).render("PHYSICS LAB", True, (0, 255, 100))
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 100))
    
    # TODO: Add menu later
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
