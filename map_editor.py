import pygame, sys, math
from textures import *
from map_editor import *

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



window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()


txt_font = pygame.font.Font("/home/griffin/Ubuntu-LI.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * Tiles.size, 100 * Tiles.size


selector = pygame.Surface((Tiles.size, Tiles.size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill((255,255,255,50))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0


brush = "5"



# Initialize Default Map
tile_data = generate()




isRunning = True


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
            if event.key == pygame.K_F4:
                brush = "r"
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


        elif event.type == pygame.KEYUP:
            camera_move = 0

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

            # If this tile space is empty
            if not found:
                if not brush == "r":
                    tile_data.append(tile)

            # If this tile space is not empty
            else:
                # Are we using the rubber tool?
                if brush == "r":
                    # Remove Tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Tile Removed!")

                else:
                    # Sorry! A tile is already placed here!
                    print("A tile is already placed here!")




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

    window.fill((0,0,255))


    # Draw Map
    for tile in tile_data:
        try:
            window.blit(Tiles.texture_tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass


    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))



    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
