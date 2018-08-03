#!/usr/bin/env python2

"""
OO framework to encapsulate the logic behind the problem and provide a hopefully
somewhat enlightening visual representation of said logic
"""

from itertools import chain

from pure_utils import ilog2, power_of_two, find_money, generate_bits

# set of light legible colours - bytes are ARGB
LEGIBLE_COLOURS = [
    0xFF46BCDE,
    0xFF52D273,
    0xFFE94F64,
    0xFFE57254,
    0xFFE5C454,
    0xFFffbdbd,
    0xFFc9c9ff,
    0xFFf1cbff,
    0xFFe1f7d5,
]

# size of the mark indicating a target
T_MARK_SIZE = 0.5

def centred_ellipse(x, y):
    """
    Draw a centred unit ellipse at (x, y), subsequently returning to CORNER mode
    """
    ellipseMode(CENTER)
    ellipse(x + 0.5, y + 0.5, T_MARK_SIZE, T_MARK_SIZE)
    ellipseMode(CORNER)

def multic_text(x, y, *txt):
    """
    Utility function to draw a line of multicoloured text. Takes a starting x
    and y, and then all further arguments should be either a string or a colour
    to switch to.
    """
    for c in txt:
        if isinstance(c, str):
            text(c, x, y)
            x += textWidth(c)
        else:
            fill(c)

class TileTrick(object):
    """
    Class that tracks the actual bits and does the calculations, and also
    provides the visual representation, along with tracking necessary parameters
    for that.
    """
    __slots__ = """n bits bit_colours w h w_t h_t tb_x tb_y unit b_unit cards
                   font
                """.split()

    def __init__(self, n, width, height, tb_x, tb_y, font):
        """
        Initialise class, given
        - size of board
        - permitted width to draw the board on
        - permitted height to draw the board on
        - textbox co-ordinates for textual explanation
        - font to use for text. Use fixed-width (eg courier) for best results
        """
        self.w_t = width
        self.h_t = height
        self.tb_x = tb_x
        self.tb_y = tb_y
        self.font = font
        self.set_size(n)

    def target(self):
        """
        Get the current "target" of the board
        """
        return find_money(self.cards)

    def set_size(self, value):
        """
        Set the board size to `value` (performing appropriate checks) and then
        set all appropriate parameters.
        """
        colorMode(HSB, 255, 255, 255)
        self.n = power_of_two(value)
        # binary number of bits on board and colour for each group
        self.bits = ilog2(self.n)
        self.bit_colours = LEGIBLE_COLOURS[:self.bits]
        self.bit_colours.extend([0xFFFFFFFF] * (self.bits - len(self.bit_colours)))
        self.b_unit = 1 / float(self.bits)
        # unit size of each tile, and width and height in these units
        self.h = 1 << (self.bits >> 1)
        self.w = self.n // self.h
        self.unit = min(self.w_t / self.w, self.h_t / self.h)
        # initialise tiles
        self.zero()

    def draw(self, mx, my):
        """
        Draw the board, using Processing's primitives and take the mouse
        position into account.
        """
        background(0x353535)
        noStroke()
        ellipseMode(CORNER)
        pushMatrix()
        colorMode(RGB, 255, 255, 255)
        scale(self.unit)
        target = self.target()
        self.click(mx, my, LEFT)
        # speculative target if the user clicks
        mod_target = self.target()
        self.click(mx, my, LEFT)
        umx = mx // self.unit
        umy = my // self.unit
        if 0 <= umx < self.w and 0 <= umy < self.h:
            mouseloc = umy * self.w + umx
        else:
            mouseloc = -1
        # Draw each tile
        for x in xrange(self.w):
            for y in xrange(self.h):
                ind = y * self.w + x
                # a tile being hovered over "dims" itself
                full_fill = 0xDD if ind != mouseloc else 0xCC
                # determine which colours to use
                if self.cards[ind]:
                    # alpha value to use for bit group rectangles
                    group_alpha = 255
                else:
                    full_fill = 255 - full_fill
                    group_alpha = 100
                fill(255 - full_fill)
                rect(x, y, 1, 1) # inverted background rectangle
                fill(full_fill)
                ellipse(x, y, 1, 1)
                # draw small circles on the targets
                if ind == mod_target:
                    fill(0, 255, 0)
                    centred_ellipse(x, y)
                elif ind == target:
                    fill(255, 0, 0)
                    centred_ellipse(x, y)
                # draw the bit group rectangles
                for bit, clr in enumerate(self.bit_colours):
                    if (1 << bit) & ind:
                        # induce the alpha by bit-hacking
                        fill(clr & (((group_alpha + 1) << 24) - 1))
                        rect(x + 1 - float(bit + 1) / self.bits, y,
                             self.b_unit, self.b_unit)
        popMatrix()
        # draw the calculation text
        textFont(self.font)
        # the maximum possible membership of any group
        pad_size = len(str(self.n >> 1))
        multic_text(self.tb_x, self.tb_y, color(0xDD),
                    "     bit groups: ",
                    *chain(*((colour,
                      "{:{p}},".format(1 << bit, p=pad_size))
                           for bit, colour in
                           reversed(list(enumerate(self.bit_colours))))))
        multic_text(self.tb_x, self.tb_y + 20, color(0xDD),
                    "   group totals: ",
                    *chain(*((colour,
                      "{:{p}},".format(
                        sum(i for ind, i in enumerate(self.cards)
                            if ind & (1 << bit)), p=pad_size))
                           for bit, colour in
                           reversed(list(enumerate(self.bit_colours))))))
        multic_text(self.tb_x, self.tb_y + 40, color(0xDD),
                    " group parities: ",
                    *chain(*((colour,
                        "{:{p}},".format(((target >> bit) & 1), p=pad_size))
                           for bit, colour in
                           reversed(list(enumerate(self.bit_colours))))))
        fill(0xDD)
        text(       "resulting index: {:{}}".format(target, len(str(self.n))),
             self.tb_x, self.tb_y + 60)

    def randomise(self):
        """
        Randomise the board
        """
        self.cards = generate_bits(self.n)

    def zero(self, one=False):
        """
        Set all cards to 0
        """
        self.cards = [1 if one else 0] * self.n

    def click(self, mx, my, btn):
        """
        Handle a mouse click at specified location. Left click on square flips,
        it, right click on square makes it the target with one flip.
        """
        x = mx // self.unit
        y = my // self.unit
        if 0 <= x < self.w and 0 <= y < self.h:
            if btn == LEFT:
                self.cards[y * self.w + x] ^= 1
            elif btn == RIGHT:
                self.cards[(y * self.w + x) ^ self.target()] ^= 1
