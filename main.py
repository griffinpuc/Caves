import pygame, sys, time, math
from pygame.locals import *
from textures import *
from mapengine import *
from player import *
from globals import *

pygame.init()

#Vars
csec = 0
cframe = 0
fps = 0
tile_data = MapEngine.load_map("maps/tester.map")

#Set Sky?
sky = pygame.image.load("textures/sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

selector = pygame.Surface((Tiles.size, Tiles.size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill((255,255,255,50))

#Functions
def create_window():
    global window, window_width, window_height, clock
    window_width = 1000
    window_height = 800
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    pygame.display.set_caption('Not Sure Yet')
    clock = pygame.time.Clock()

def count_fps():
    global fps
    fps = clock.get_fps()

create_window()
player = Player("griffin")
player_width, player_height = player.width, player.height
player_x = (window_width / 2 - player_width / 2 - Globals.camera_x) / Tiles.size
player_y = (window_height / 2 - player_height / 2 - Globals.camera_y) / Tiles.size

#Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
                player.facing = "east"
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                player.facing = "west"
        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0

    #Logic
    if Globals.camera_move ==1:
        if not Tiles.blocked_at((round(player_x), math.floor(player_y))):
            Globals.camera_y += 1
    elif Globals.camera_move == 2:
        if not Tiles.blocked_at((round(player_x), math.ceil(player_y))):
            Globals.camera_y -= 1
    elif Globals.camera_move == 3:
        if not Tiles.blocked_at((math.floor(player_x), round(player_y))):
            Globals.camera_x += 1
    elif Globals.camera_move == 4:
        if not Tiles.blocked_at((math.ceil(player_x), round(player_y))):
            Globals.camera_x -= 1

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        for t in tile_data:
            if t[0] == tile[0] and t[1] == tile[1]:
                tile_data.remove(t)

    mouse_x, mouse_y = 0, 0
    if event.type == pygame.MOUSEMOTION:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = math.floor(mouse_pos[0] / Tiles.size) * Tiles.size
        mouse_y = math.floor(mouse_pos[1] / Tiles.size) * Tiles.size

    player_x = (window_width / 2 - player_width / 2 - Globals.camera_x) / Tiles.size
    player_y = (window_height / 2 - player_height / 2 - Globals.camera_y) / Tiles.size

    #Sky
    window.blit(Sky, (0, 0))

    #Map
    for tile in tile_data:
        try:
            window.blit(Tiles.texture_tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass
    window.blit(selector, (mouse_x, mouse_y))

    #Player
    player.render(window, (window_width / 2 - player_width / 2, window_height / 2 - player_height / 2))

    pygame.display.update()
    clock.tick()
    count_fps()

pygame.quit()
sys.exit()
