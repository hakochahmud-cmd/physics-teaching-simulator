import pygame

# Retro style settings
WIDTH, HEIGHT = 1024, 768
FPS = 60
TITLE = "Physics Lab - Retro Simulator"

# Colors (retro palette)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)

pygame.font.init()
FONT_SMALL = pygame.font.SysFont("consolas", 18)
FONT_MED = pygame.font.SysFont("consolas", 24)
FONT_BIG = pygame.font.SysFont("consolas", 36)
