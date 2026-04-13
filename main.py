import pygame
from import_sprites import load_all_sprites  

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

sprites = load_all_sprites(size=(96, 96))

anim_timer = 0
anim_frame = 0
speed = 400  

running = True
while running:
    dt = clock.tick(60)
    anim_timer += dt

    if anim_timer >= speed:
        anim_timer = 0
        anim_frame = (anim_frame + 1) % 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(('green'))

    x = 20
    for name, frames in sprites.items():
        frame = frames[anim_frame % len(frames)]
        screen.blit(frame, (x, 250))
        x += 100

    pygame.display.flip()

pygame.quit()