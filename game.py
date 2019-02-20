import pygame, sys, math, time
from textures import *
from globals import *
from player import *
from tkinter import *
from mapengine import *
from terrain_gen import *

'''
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

def load_map(file):
    global tile_data
    with open(file, "r") as mapfile:
        map_data = mapfile.read()
    map_data = map_data.split("-")
    map_size = map_data[len(map_data) - 1]
    map_data.remove(map_size)
    map_size = map_size.split(",")
    map_size[0] = int(map_size[0]) * Tiles.size
    map_size[1] = int(map_size[1]) * Tiles.size

    tiles = []

    for tile in range(len(map_data)):
        map_data[tile] = map_data[tile].replace("\n", "")
        tiles.append(map_data[tile].split(":"))

    for tile in tiles:
        tile[0] = tile[0].split(",")
        pos = tile[0]
        for p in pos:
            pos[pos.index(p)] = int(p)
        tiles[tiles.index(tile)] = [pos[0] * Tiles.size, pos[1] * Tiles.size, tile[1]]

    tile_data = tiles
'''


window = pygame.display.set_mode((1600, 1000), pygame.HWSURFACE)
pygame.display.set_caption("Torchlight")
clock = pygame.time.Clock()

mouse_pos = 0
mouse_x, mouse_y = 0, 0
map_width, map_height = 4800, 3600
window_width, window_height = 1600, 1000
selector = pygame.Surface((Tiles.size, Tiles.size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill((255,255,255,50))
camera_x, camera_y = 0, 0
camera_move = 0
brush = ""

# Initialize Default Map
tile_data = generate()

isRunning = True
x1, y1 = coords[0], coords[1]
direction = 0
player2 = Tiles.load_texture("textures/ruby.png", Tiles.size)

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:

            # MOVEMENT
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4

            # BRUSHES
            elif event.key == pygame.K_F1:
                selection = input("Brush Tag: ")
                brush = selection


            # SAVE MAP
            if event.key == pygame.K_F11:
                name = input("Map Name: ")
                export_map(name + ".map")
                print("Map Saved Successfully!")

            elif event.key == pygame.K_F10:
                name = input("Map Name: ")
                load_map("maps/" + name + ".map")
                print("Map Loaded Successfully")

            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_RIGHT:
                direction = 2

        elif event.type == pygame.KEYUP:
            camera_move = 0
            direction = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / Tiles.size) * Tiles.size
            mouse_y = math.floor(mouse_pos[1] / Tiles.size) * Tiles.size

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush]   # Keep this as a list

            # Is a tile already placed here?
            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1]:
                    found = True
                    break
            if event.button == 3:
                # If this tile space is empty
                if not found:
                    tile_data.append(tile)
                else:
                    pass

            if event.button == 1:
                # If this tile space is not empty
                for t in tile_data:
                    if t[0] == tile[0] and t[1] == tile[1]:
                        tile_data.remove(t)
                        print("Tile Removed!")
                    else:
                        pass

    found = False
    for t in tile_data:
        if t[0] == x1 and t[1] == y1:
            found = True
            break
    if not found:
        y1 += Tiles.size * .50 # Falling Speed

    # LOGIC
    if camera_move == 1:
        camera_y += Tiles.size
    elif camera_move == 2:
        camera_y -= Tiles.size
    elif camera_move == 3:
        camera_x += Tiles.size
    elif camera_move == 4:
        camera_x -= Tiles.size



    # RENDER GRAPHICS

    window.fill((0,0,20))
    for x in range(0, 4800, Tiles.size):
        for y in range(0, 3600, Tiles.size):
            window.blit(Tiles.stone_background, (x, y))

    # Draw Map
    for tile in tile_data:
        try:
            window.blit(Tiles.texture_tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))
    if direction == 1:
        if not Tiles.blocked_at([x1, y1]):
            x1-= Tiles.size
            print("moved 1")
        else:
            print("cant 1")
    elif direction == 2:
        if not Tiles.blocked_at([x1, y1]):
            x1+= Tiles.size
            print("moved 2")
        else:
            print("cant 2")
    window.blit(player2, (x1, y1 - Tiles.size))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
