import pygame
import random
from textures import *
from caves import *

Tiles.size = 48
tile_data = []
coords = []

map_width = 100
map_height = 75


def generate():
    global coords, tile_data
    coordsx, coordsy = 0, 0
    tile_data = []
    coords = []
    searching = True
    print("Generating...")
    for y in range(0, map_width, 1):
        for x in range(0, map_height, 1):
            if caveMap[x][y]:
                if random.randint(1, 10) > 7 and y * Tiles.size > 864:
                    tile_data.append([x * Tiles.size, y * Tiles.size, "2"])
                    if random.randint(1, 10) > 8 and y * Tiles.size > 1728:
                        tile_data.append([x * Tiles.size, y * Tiles.size, "3"])
                    else:
                        tile_data.append([x * Tiles.size, y * Tiles.size, "1"])
                else:
                    tile_data.append([x * Tiles.size, y * Tiles.size, "1"])
            if not caveMap[x][y]:
                tile_data.append([x * Tiles.size, y * Tiles.size, "1"])
                tile_data.remove([x * Tiles.size, y * Tiles.size, "1"])

                iteration = 1
                while searching:
                    coords.append(x * Tiles.size)
                    coords.append(y * Tiles.size)
                    print("Player Spawned At: " + str(coords[0]) + "," + str(coords[1]))
                    searching = False
                else:
                    pass
    for tile in tile_data:
        if tile[2] in Tiles.blocked_types:
            Tiles.blocked.append([tile[0], tile[1]])
    print(Tiles.blocked)


    print("Finished.")
    return tile_data


def export_map(file):
    map_data = ""

    # Get Map Dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    # Save Map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / Tiles.size)) + "," + str(int(tile[1] / Tiles.size)) + ":" + tile[2] + "-"


    # Save Map Dimensions
    map_data = map_data + str(int(max_x / Tiles.size)) + "," + str(int(max_y / Tiles.size))


    # Write Map File
    with open("maps/" + file, "w") as mapfile:
        mapfile.write(map_data)

generate()
export_map("tester.map")
