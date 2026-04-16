import pygame
from import_sprites import load_all_sprites  

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

sprites = load_all_sprites(size=(96, 96))
