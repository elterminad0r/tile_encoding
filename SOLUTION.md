# The solution

The way to think about this is in terms of information theory. The square is
really kind of misleading. From now on, I will refer to boards as sequences of
bits, indexed from 0 to N-1 (starting from the top left and going left to right,
top to bottom).

The final idea I'm using is similar to a Hamming code, but in fact using an
extra bit. This is placed at the index 0. The reason we need this bit is in
order to have a "no-op" available - if the board already encodes for a number,
we just flip 0 and say that that also encodes for the number. The reason 0 is
suitable for this will become apparent...

We now consider the possible "groups" on the board. These work similarly to
Hamming codes, in that they require the same bits to be present, although we're
now a little less worried about encoding the parity in the message - rather, we
use the parity of each group to encode a new message. The groups for 8\*8 are as
follows:

```
group 0: each index with a 1 bit
   | X |   | X |   | X |   | X
---+---+---+---+---+---+---+---
   | X |   | X |   | X |   | X
---+---+---+---+---+---+---+---
   | X |   | X |   | X |   | X
---+---+---+---+---+---+---+---
   | X |   | X |   | X |   | X
---+---+---+---+---+---+---+---
   | X |   | X |   | X |   | X
---+---+---+---+---+---+---+---
   | X |   | X |   | X |   | X
---+---+---+---+---+---+---+---
   | X |   | X |   | X |   | X
---+---+---+---+---+---+---+---
   | X |   | X |   | X |   | X

group 1: each index with a 2 bit
   |   | X | X |   |   | X | X
---+---+---+---+---+---+---+---
   |   | X | X |   |   | X | X
---+---+---+---+---+---+---+---
   |   | X | X |   |   | X | X
---+---+---+---+---+---+---+---
   |   | X | X |   |   | X | X
---+---+---+---+---+---+---+---
   |   | X | X |   |   | X | X
---+---+---+---+---+---+---+---
   |   | X | X |   |   | X | X
---+---+---+---+---+---+---+---
   |   | X | X |   |   | X | X
---+---+---+---+---+---+---+---
   |   | X | X |   |   | X | X

group 2: each index with a 4 bit
   |   |   |   | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   | X | X | X | X

group 3: each index with a 8 bit
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X

group 4: each index with a 16 bit
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X

group 5: each index with a 32 bit
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
   |   |   |   |   |   |   |
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
---+---+---+---+---+---+---+---
 X | X | X | X | X | X | X | X
```

You may notice that each position of the board in fact represents a union of a
unique subset of these groups. This means that by "flipping" any single bit, it
is possible to "flip" any desired subset of these parity groups. This means that
we can actually change the six parities of these groups to anything we like, by
selecting the proper bit, and an accomplice now only needs to calculate the
parity of each group, and hence determine the index they point to.

This approach also shows that this trick is possible for any set of cards of
size that is a power of two. However, the odd powers of two must be arranged in
a domino. Perhaps the square layout does actually help an experienced performer,
as each of the groups has quite a regular structure.

This, while a sufficient proof of feasibility is a little laborious and doesn't
really roll off the tongue. Fortunately, several components of this problem are
pretty much isomorphic to the XOR operation (represented by `XOR` or &oplus;), a
commonly implemented bit-twiddling technique. The XOR operation is essentially
used to "flip" bits. `A XOR B` represents the
[exclusive disjunction](https://en.wikipedia.org/wiki/Exclusive_or) of A and B.

Normally, we can rely on the presence of a "bitwise XOR" (represented by `XOR`
or `^`, which takes two integers as input, and returns the integer that you get
when you XOR each pair of bits in the same place value, eg `234 ^ 438 == 348`:

```
   11101010
^ 110110110
= 101011100
```

XOR in this sense has some interesting properties.
`S_0 XOR S_1 XOR S_2 XOR ... XOR S_n` actually represents the parity of the
sequence S. By using bitwise XOR, we can simultaneously compute the parity of
each bit position, which is in fact what we need for this Hamming code to work.

A more obvious argument, which would be less obvious to derive, uses the fact
that `A ^ A == 0`, and that the XOR operation is commutative. We first compute
the "folded bitwise XOR" of sequence of indices which currently store a 1: `X(S)
= S_0 ^ S_1 ^ ... ^ S_n`, and then we calculate, with respect to the target
index T, the flip index F: `F = X(S) ^ T` After flipping F to produce a new
sequence `S'`, we note that `X(S') = X(S) ^ X(S) ^ T = T`. Hence, the accomplice
simply needs to calculate this folded bitwise XOR of the received sequence to
arrive at the desired index.

This argument results in an almost disappointingly concise implementation:

```python
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
```

Yes, that's about 2 core LoC. The feasibility of a human performing this in
limited time is still questionable, but the algorithm works.

The provided script `magic_encode.py` also provides some other functionality:
nicely formatted boards, the dimensions of which are automatically calculated
with a little exponential integer arithmetic, which you may have noticed
earlier, and the automatic generation of random bits, against which it then
tests itself for each index, failing if an error occurs. It is a command-line
script so must be run from a shell in a terminal. Here it is in action:

```
$ python magic_encode.py 32
the board is:
 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1
---+---+---+---+---+---+---+---
 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0
---+---+---+---+---+---+---+---
 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1
---+---+---+---+---+---+---+---
 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0

flipping index  6 encodes  0 - correctly guessed  0
flipping index  7 encodes  1 - correctly guessed  1
flipping index  4 encodes  2 - correctly guessed  2
flipping index  5 encodes  3 - correctly guessed  3
flipping index  2 encodes  4 - correctly guessed  4
flipping index  3 encodes  5 - correctly guessed  5
flipping index  0 encodes  6 - correctly guessed  6
flipping index  1 encodes  7 - correctly guessed  7
flipping index 14 encodes  8 - correctly guessed  8
flipping index 15 encodes  9 - correctly guessed  9
flipping index 12 encodes 10 - correctly guessed 10
flipping index 13 encodes 11 - correctly guessed 11
flipping index 10 encodes 12 - correctly guessed 12
flipping index 11 encodes 13 - correctly guessed 13
flipping index  8 encodes 14 - correctly guessed 14
flipping index  9 encodes 15 - correctly guessed 15
flipping index 22 encodes 16 - correctly guessed 16
flipping index 23 encodes 17 - correctly guessed 17
flipping index 20 encodes 18 - correctly guessed 18
flipping index 21 encodes 19 - correctly guessed 19
flipping index 18 encodes 20 - correctly guessed 20
flipping index 19 encodes 21 - correctly guessed 21
flipping index 16 encodes 22 - correctly guessed 22
flipping index 17 encodes 23 - correctly guessed 23
flipping index 30 encodes 24 - correctly guessed 24
flipping index 31 encodes 25 - correctly guessed 25
flipping index 28 encodes 26 - correctly guessed 26
flipping index 29 encodes 27 - correctly guessed 27
flipping index 26 encodes 28 - correctly guessed 28
flipping index 27 encodes 29 - correctly guessed 29
flipping index 24 encodes 30 - correctly guessed 30
flipping index 25 encodes 31 - correctly guessed 31
flipped 32 distinct bits
```

You may inspect the source to verify that it does not cheat.
