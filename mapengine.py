import pygame

from textures import *

#Map Format:
#x,y:id-

class MapEngine:

    def add_tile(tile, pos, addTo):
        addTo.blit(tile, (pos[0] * Tiles.size, pos[1] * Tiles.size))

    def load_map(file):
        #Open Map File
        with open(file, "r") as mapfile:
            map_data = mapfile.read()

        #Load Map Data
        map_data = map_data.split("-")
        map_size = map_data[len(map_data) - 1] #Get Dimensions
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * Tiles.size
        map_size[1] = int(map_size[1]) * Tiles.size

        tiles = []

        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":"))
        for tile in tiles:
            tile[0] = tile[0].split(",") #Split Pos Into List
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p)
            tiles[tiles.index(tile)] = (pos, tile[1]) #Save To Tile List

        #Create Terrain
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)
        for tile in tiles:
            if tile[1] in Tiles.texture_tags:
                MapEngine.add_tile(Tiles.texture_tags[tile[1]], tile[0], terrain)
            if tile[1] in Tiles.blocked_types:
                Tiles.blocked.append(tile[0])
        return tiles
