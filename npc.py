import pygame

pygame.init()

def get_faces(sprite):
    faces = {}
    size = sprite.get_size()
    tile_size = (int(size[0] / 2), int(size[1] / 2))

    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0, 0), (0, 0, tile_size[0], tile_size[1]))
    faces["south"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0, 0), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
    faces["north"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
    faces["east"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0, 0), (0, tile_size[1], tile_size[0], tile_size[1]))
    faces["west"] = west

    return faces
