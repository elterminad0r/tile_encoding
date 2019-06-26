"""
The main processing app, that basically provides the interface to a TileTrick.

Further information can be found in DOCUMENTATION.md
"""

from visual_utils import TileTrick

DEFAULT_SIZE = 32

save_frames = False

def setup():
    global game
    size(1280, 720)
    game = TileTrick(DEFAULT_SIZE,
                     width / 2, height, width / 2 + 50, 50,
                     createFont("courier", 20, True))
    game.randomise()

def draw():
    game.draw(mouseX, mouseY)
    if save_frames:
        saveFrame("frames/encoding-########.png")

def keyPressed():
    global save_frames
    if keyCode == UP:
        game.set_size(game.n << 1)
        game.randomise()
    elif keyCode == DOWN:
        if game.n > 2:
            game.set_size(game.n >> 1)
            game.randomise()
    elif keyCode == ord("R"):
        game.randomise()
    elif ord("0") <= keyCode <= ord("9"):
        game.set_size(2 << (keyCode - ord("0")))
        game.randomise()
    elif keyCode == ord("Z"):
        game.zero()
    elif keyCode == ord("W"):
        game.zero(True)
    elif keyCode == ord(" "):
        save_frames = not save_frames
        print("save_frames: {}".format(save_frames))

def mouseClicked():
    game.click(mouseX, mouseY, mouseButton)
