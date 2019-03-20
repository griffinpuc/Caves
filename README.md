# Caves

&nbsp;&nbsp;&nbsp;&nbsp;Python application that creates a 2D underground cave world using cellular automata. The start to a game that was never finished. Made in the summer of 2017 due to boredom.

&nbsp;

## How it works:
1. [main.py](https://github.com/griffinpuc/Caves/blob/master/main.py) > The main game loop
2. [terrain_gen.py](https://github.com/griffinpuc/Caves/blob/master/terrain_gen.py) > The cellular automata algorithm
3. [textures.py](https://github.com/griffinpuc/Caves/blob/master/textures.py) > Texture handler
4. [map_editor.py](https://github.com/griffinpuc/Caves/blob/master/map_editor.py) > Controls for camera moving and destroying and placing blocks, saving and loading maps

&nbsp;

## Notes

&nbsp;&nbsp;&nbsp;&nbsp;Lots of obsolete code and bugs. There isn't much functionality- the only part of this worth saving is the [terrain_gen.py](https://github.com/griffinpuc/Caves/blob/master/terrain_gen.py) file and [map_editor.py](https://github.com/griffinpuc/Caves/blob/master/map_editor.py) for the terrain generating and file saving/loading functionality. Everything else should be scrapped and re-written for future use, the main engine is a mess.

&nbsp;

## Possible future implementation:

### Finished:
- [x] Cellular automata algorithm
- [x] Custom world filetype for importing and exporting world saves
- [x] Destroying and placing various types of blocks within the world grid

### Planned:
- [ ] Re-write main game loop
- [ ] Remove obsolete code
- [ ] Re-write camera and player code
- [ ] Finish gravity implementation **(Half finished)**
- [ ] Proper start menu
- [ ] In-game menu
- [ ] More expansive underground 2D world
