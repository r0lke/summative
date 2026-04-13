# import_sprites.py
import os
import pygame

SPRITES_DIR = os.path.join("assets", "spirit    s")  # у тебя spirits, не sprites!

def load_sprite(filename, size=(96, 96)):
    path = os.path.join(SPRITES_DIR, filename)
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, size)

def load_all_sprites(size=(96, 96)):
    sprites = {
        "slime":      [load_sprite("monster_slime.png",    size),
                       load_sprite("slime_v2.png",          size)],

        "skeleton":   [load_sprite("monster_skeleton.png", size),
                       load_sprite("skeleton_v2.png",       size)],

        "goblin":     [load_sprite("monster_goblin.png",   size),
                       load_sprite("goblin_v2.png",         size)],

        "ghost":      [load_sprite("monster_ghost.png",    size),
                       load_sprite("ghost_v2.png",          size)],

        "spider":     [load_sprite("monster_spider.png",   size),
                       load_sprite("spider_v2.png",         size)],

        "dragon":     [load_sprite("monster_dragon.png",   size),
                       load_sprite("dragon_v2.png",         size)],

        "vampire":    [load_sprite("monster_vampire.png",  size),
                       load_sprite("vampire_v2.png",        size)],

        "golem":      [load_sprite("monster_golem.png",    size),
                       load_sprite("golem_v2.png",          size)],

        "witch":      [load_sprite("monster_witch.png",    size),
                       load_sprite("witch_v2_fixed.png",    size)],

        "demon_boss": [load_sprite("monster_demon_boss.png", size),
                       load_sprite("demon_boss_v2.png",       size)],

        "hero":       [load_sprite("hero_player.png",      size),
                       load_sprite("hero_v2.png",           size)],
    }
    return sprites