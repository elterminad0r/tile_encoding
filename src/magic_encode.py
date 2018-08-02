#!/usr/bin/env python3

"""
Program that performs real magic - see README.md and SOLUTION.md.
By default, it will generate a random board, and then test each possible square
to see if the algorithm works. It doesn't cheat, and will actually fail
critically if it gets a single guess wrong.
"""

import sys

from functools import reduce
from operator import xor
from random import randrange, choices
from itertools import count
from argparse import ArgumentParser, FileType

# start of core problem logic:

def find_money(bits):
    """
    Return the index currently pointed to by the log2(|bits|) "Hamming" bits.
    """
    return reduce(xor, (ind for ind, bit in enumerate(bits) if bit), 0)

def generate_flip(bits, target):
    """
    Generate which bit to flip in order to change the target to `target`.
    """
    return target ^ find_money(bits)

# end of core problem logic. scripting bureaucracy from here

def isqrt(n):
    """
    Calculate the integer square root of a number using the "bit-shift"
    algorithm.
    """
    if n < 2:
        return n
    small = isqrt(n >> 2) << 1
    large = small + 1
    if large ** 2 > n:
        return small
    return large

def ilog2(n):
    """
    Return the integer log2 by bitshifting
    """
    for i in count():
        n >>= 1
        if not n:
            return i
    return 0 # linter complains

def power_of_two(arg):
    """
    Bit twiddling to determine if a string represents an integer power of two.
    """
    n = int(arg)
    if n <= 0 or n & (n - 1):
        raise ValueError("not a power of two")
    return n

def get_args():
    """
    Parse argv
    """
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "size", type=power_of_two, help="Number of bits to do the trick with")
    parser.add_argument(
        "--test-fmt", action="store_true",
        help="Test the rectangle-formatting capabilities of the program")
    return parser.parse_args()

def make_rectangle(w, h):
    """
    Generate a .format-string to display a rectangular arrangement of w*h
    str-compatible items. Only works if they have length 1
    """
    return (
        "\n{}\n".format("+".join(["---"] * w))
        .join(["|".join([" {} "] * w)] * h) + "\n"
    )

def test_rectangles():
    """
    Test some configurations of rectangle
    """
    for w in range(1, 5):
        for h in range(1, 5):
            print("{} * {}:".format(w, h))
            print(make_rectangle(w, h).format(*choices(" X", k=w * h)))

def generate_bits(size):
    """
    Generate n random bits
    """
    return [randrange(2) for _ in range(size)]

def test_board(size):
    """
    Test each possible square for a board of a given size.
    """
    board = generate_bits(size)
    pad = len(str(size))
    h = 1 << (ilog2(size) // 2)
    w = size // h
    template = make_rectangle(w, h)
    print("the board is:")
    print(template.format(*board))
    seen_idx = set()
    for i in range(size):
        idx = generate_flip(board, i)
        print("flipping index {:{pad}} encodes {:{pad}}"
              .format(idx, i, pad=pad), end=" ")
        board[idx] = not board[idx]
        guess = find_money(board)
        if idx in seen_idx:
            print("- incorrect: this index was previously used")
            sys.exit(1)
        else:
            seen_idx.add(idx)
        if guess != i:
            print("- incorrect guess: {:{pad}} should be {:{pad}}"
                  .format(guess, i, pad=pad))
            print(template.format(*board))
            sys.exit(1)
        print("- correctly guessed {:{pad}}".format(guess, pad=pad))
        board[idx] = not board[idx]
    print("flipped {} distinct bits".format(len(seen_idx)))

if __name__ == "__main__":
    ARGS = get_args()
    if ARGS.test_fmt:
        test_rectangles()
    else:
        test_board(ARGS.size)
