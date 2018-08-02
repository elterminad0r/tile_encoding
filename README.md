# tile\_encodings
Solving the following problem:

Given a series of N random bits (N could be 4 or 64), toggle exactly one bit
such that you have encoded an integer in {0..N-1}.

Phrased as a magic trick, you arrange for example 64 cards which are black on
one side, and white on the other in a square. You let the target randomly flip
all of the cards, and then select a particular cards (say, by placing some money
under it). You then flip exactly one card. At this point, your accomplice, who
has been out of the room the whole time, comes in and "immediately" determines
which card is the target. This involves no tricks (well, a bit of information
theory).

This repository contains [programs to solve][1] this problem, and a
[document detailing my exact solution][2].

[1]: https://github.com/elterminad0r/tile_encodings/blob/master/src/magic_encode.py
[2]: https://github.com/elterminad0r/tile_encodings/blob/master/SOLUTION.md
