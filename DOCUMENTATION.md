# Processing sketch documentation

Also implemented is a graphical/interactive applet/sketch in the Processing
framework. To run it you need Processing with Python mode installed. Below are
some screenshots at different scales:

![screenshot](https://github.com/elterminad0r/tile_encoding/blob/master/win_screenshot_20180803_170728.png)
![screenshot](https://github.com/elterminad0r/tile_encoding/blob/master/win_screenshot_20180803_170923.png)

The program draws the "board" and then adds some clutter. A tile with a light
central circle is thought of as a 1.

Each tile has some set of coloured squares above it. These represents the
Hamming parity groups. These squares are actually just the binary representation
of the number, coloured by place value. This is how the squares are arranged.

An "on" tile will "contribute" to that groups total, as seen on the right. These
totals are then taken modulo two (we look if they are even or odd). This gives
an n-digit binary number, which we then finally use to point to the index with
the money. This program aims to show how this calculation happens and how it can
be influenced by magician A.

The current location of the money is represented by a red dot. When hovering
over a tile, a green dot represents where the money will be after you click.

Under the hood, it uses the same approach as the command-line script, with all
of the XOR stuff. This is really just geek-speak for a certain efficient binary
operation to implement this approach, and doesn't really pertain much to the
maths here.

Usage:

| Action | Effect                                                      |
|--------|-------------------------------------------------------------|
| UP     | Increase board size by a factor 2                           |
| DOWN   | Decrease board size by a factor 2 (with a lower limit of 1) |
| R      | Randomise board                                             |
| 0-9    | Jump to board size of a certain power of 2                  |
| Z      | "zero" the board - set all to black                         |
| Z      | "white" the board - set all to white                        |
| SPACE  | Start/stop recording frames (for making videos)             |
| LCLICK | Flip the tile under the mouse                               |
| RCLICK | Make the tile under the mouse the target (do the trick)     |

Also provided is a [video](https://youtu.be/221aW0WzvVI) of it in action.
