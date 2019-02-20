import pygame

pygame.init()

class Tiles:
    size = 48
    blocked = []
    blocked_types = [
        "1",
        "2",
        "3"
    ]

    def blocked_at(pos):
        if list(pos) in Tiles.blocked:
            return True
        else:
            return False

    #Texture Function
    def load_texture(file, size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (size, size))
        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

    #Load Textures
    stone = load_texture("textures/stone.png", size)
    ruby = load_texture("textures/ruby.png", size)
    sapphire = load_texture("textures/sapphire.png", size)
    stone_background = load_texture("textures/stone_background.png", size)
    torch = load_texture("textures/torch.png", size)


    texture_tags = {
    "1":stone,
    "2":ruby,
    "3":sapphire,
    "4":stone_background,
    "5":torch
    }
