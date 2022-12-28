# --- Day 22: Monkey Map ---
#
# The monkeys take you on a surprisingly easy trail through the
# jungle.  They're even going in roughly the right direction according
# to your handheld device's Grove Positioning System.
#
# As you walk, the monkeys explain that the grove is protected by a
# force field.  To pass through the force field, you have to enter a
# password; doing so involves tracing a specific path on a
# strangely-shaped board.
#
# At least, you're pretty sure that's what you have to do; the
# elephants aren't exactly fluent in monkey.
#
# The monkeys give you notes that they took when they last saw the
# password entered (your puzzle input).
#
# For example:
#
#         ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
#
# 10R5L5R10L4R5L5
#
# The first half of the monkeys' notes is a map of the board.  It is
# comprised of a set of open tiles (on which you can move, drawn .)
# and solid walls (tiles which you cannot enter, drawn #).
#
# The second half is a description of the path you must follow.  It
# consists of alternating numbers and letters:
#
# - A number indicates the number of tiles to move in the direction
#   you are facing.  If you run into a wall, you stop moving forward
#   and continue with the next instruction.
# - A letter indicates whether to turn 90 degrees clockwise (R) or
#   counterclockwise (L).  Turning happens in-place; it does not
#   change your current tile.
#
# So, a path like 10R5 means "go forward 10 tiles, then turn clockwise
# 90 degrees, then go forward 5 tiles".
#
# You begin the path in the leftmost open tile of the top row of
# tiles.  Initially, you are facing to the right (from the perspective
# of how the map is drawn).
#
# If a movement instruction would take you off of the map, you wrap
# around to the other side of the board.  In other words, if your next
# tile is off of the board, you should instead look in the direction
# opposite of your current facing as far as you can until you find the
# opposite edge of the board, then reappear there.
#
# For example, if you are at A and facing to the right, the tile in
# front of you is marked B; if you are at C and facing down, the tile
# in front of you is marked D:
#
#         ...#
#         .#..
#         #...
#         ....
# ...#.D.....#
# ........#...
# B.#....#...A
# .....C....#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
#
# It is possible for the next tile (after wrapping around) to be a
# wall; this still counts as there being a wall in front of you, and
# so movement stops before you actually wrap to the other side of the
# board.
#
# By drawing the last facing you had with an arrow on each tile you
# visit, the full path taken by the above example looks like this:
#
#         >>v#
#         .#v.
#         #.v.
#         ..v.
# ...#...v..v#
# >>>v...>#.>>
# ..#v...#....
# ...>>>>v..#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
#
# To finish providing the password to this strange input device, you
# need to determine numbers for your final row, column, and facing as
# your final position appears from the perspective of the original
# map.  Rows start from 1 at the top and count downward; columns start
# from 1 at the left and count rightward.  (In the above example, row
# 1, column 1 refers to the empty space with no tile on it in the
# top-left corner.)  Facing is 0 for right (>), 1 for down (v), 2 for
# left (<), and 3 for up (^).  The final password is the sum of 1000
# times the row, 4 times the column, and the facing.
#
# In the above example, the final row is 6, the final column is 8, and
# the final facing is 0.  So, the final password is
# 1000 * 6 + 4 * 8 + 0: 6032.
#
# Follow the path given in the monkeys' notes.  What is the final
# password?

import re

def load():
    part1, part2 = open("22.in").read().split("\n\n")
    lines = part1.split("\n")
    max_len = max(len(l) for l in lines)
    map = ["{:{width}}".format(l, width=max_len) for l in lines]
    path = [
        int(inst) if inst.isdigit() else inst
        for inst in re.split(
            "(?<=[LR])(?=[0-9])|(?<=[0-9])(?=[LR])",
            part2.strip()
        )
    ]
    return map, path

map, path = load()
H, W = len(map), len(map[0])  # map dimensions, including voids

WALL, OPEN, VOID = "#. "

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
R, D, L, U = range(4)  # right, down, left, up; indices into the above

def next_pos(r, c, dir):
    nr, nc = r, c
    while True:
        nr, nc = (nr+directions[dir][0])%H, (nc+directions[dir][1])%W
        if map[nr][nc] == WALL:
            return (r, c, dir)
        elif map[nr][nc] == OPEN:
            return (nr, nc, dir)
        else:
            pass  # in void; keep walking

def solve():
    r, c = 0, map[0].index(OPEN)
    dir = R
    for inst in path:
        if type(inst) is int:
            for _ in range(inst):
                r, c, dir = next_pos(r, c, dir)
        else:
            if inst == "L":
                dir = (dir-1)%4
            else:
                dir = (dir+1)%4
    print(1000*(r+1) + 4*(c+1) + dir)

solve()

# --- Part Two ---
#
# As you reach the force field, you think you hear some Elves in the
# distance.  Perhaps they've already arrived?
#
# You approach the strange input device, but it isn't quite what the
# monkeys drew in their notes.  Instead, you are met with a large
# cube; each of its six faces is a square of 50x50 tiles.
#
# To be fair, the monkeys' map does have six 50x50 regions on it.  If
# you were to carefully fold the map, you should be able to shape it
# into a cube!
#
# In the example above, the six (smaller, 4x4) faces of the cube are:
#
#         1111
#         1111
#         1111
#         1111
# 222233334444
# 222233334444
# 222233334444
# 222233334444
#         55556666
#         55556666
#         55556666
#         55556666
#
# You still start in the same position and with the same facing as
# before, but the wrapping rules are different.  Now, if you would
# walk off the board, you instead proceed around the cube.  From the
# perspective of the map, this can look a little strange.  In the
# above example, if you are at A and move to the right, you would
# arrive at B facing down; if you are at C and move down, you would
# arrive at D facing up:
#
#         ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#..A
# ..#....#....
# .D........#.
#         ...#..B.
#         .....#..
#         .#......
#         ..C...#.
#
# Walls still block your path, even if they are on a different face of
# the cube.  If you are at E facing up, your movement is blocked by
# the wall marked by the arrow:
#
#         ...#
#         .#..
#      -->#...
#         ....
# ...#..E....#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
#
# Using the same method of drawing the last facing you had with an
# arrow on each tile you visit, the full path taken by the above
# example now looks like this:
#
#         >>v#
#         .#v.
#         #.v.
#         ..v.
# ...#..^...v#
# .>>>>>^.#.>>
# .^#....#....
# .^........#.
#         ...#..v.
#         .....#v.
#         .#v<<<<.
#         ..v...#.
#
# The final password is still calculated from your final position and
# facing from the perspective of the map.  In this example, the final
# row is 5, the final column is 7, and the final facing is 3, so the
# final password is 1000 * 5 + 4 * 7 + 3 = 5031.
#
# Fold the map into a cube, then follow the path given in the monkeys'
# notes.  What is the final password?
#
# --------------------
#
# Fun puzzle!  The folding of our cube was determined by visual
# inspection and is illustrated below by face numbers and labels of
# shared edges:
#
#                 1     1
#           5     0     5
#     0.....0.....0.....0 ---> c
#
#   0       +--g--+--d--+
#   .       |     |     |
#   .       e  1  |  0  b
#   .       |     |     |
#  50       +-----+--a--+
#   .       |     |
#   .       c  2  a
#   .       |     |
# 100 +--c--+-----+
#   . |     |     |
#   . e  4  |  3  b
#   . |     |     |
# 150 +-----+--f--+
#   . |     |
#   . g  5  f
#   . |     |
# 200 +--d--+
#   |
#   |
#   v
#   r
#
# We simulate traveling on the cube by moving normally on the map, but
# detecting when we are no longer enclosed in a face.  Using the
# current face and direction, we determine the new face and new
# direction and coordinate transform.  The transforms were
# pre-calculated only by cutting out pieces of graph paper and seeing
# how they fit together!
#
# Note that cube faces are in effect butted like so:
#
#      |.|
#      |.|
#      |B|
# -----+-+
# ....A|O
# -----+
#
# The implication is that if we are at position A and move outside a
# face to position O, the transform must factor in the butting to
# return B as the next position.

from common import pick

faces = [                                # (rrange, crange)
    (range(  0,  50), range(100, 150)),  # 0
    (range(  0,  50), range( 50, 100)),  # 1
    (range( 50, 100), range( 50, 100)),  # 2
    (range(100, 150), range( 50, 100)),  # 3
    (range(100, 150), range(  0,  50)),  # 4
    (range(150, 200), range(  0,  50))   # 5
]

def face_number(r, c):
    # Return the number of the enclosing face of a position, or None.
    try:
        return pick(lambda i: r in faces[i][0] and c in faces[i][1], range(6))
    except StopIteration:
        return None

# (from face, direction) => (to face, direction, coordinate transform)
edges = {
    (2, R): (0, U, lambda r, c: (49, r+50)),    # a
    (0, D): (2, L, lambda r, c: (c-50, 99)),
    (3, R): (0, L, lambda r, c: (149-r, 149)),  # b
    (0, R): (3, L, lambda r, c: (149-r, 99)),
    (2, L): (4, D, lambda r, c: (100, r-50)),   # c
    (4, U): (2, R, lambda r, c: (c+50, 50)),
    (0, U): (5, U, lambda r, c: (199, c-100)),  # d
    (5, D): (0, D, lambda r, c: (0, c+100)),
    (1, L): (4, R, lambda r, c: (149-r, 0)),    # e
    (4, L): (1, R, lambda r, c: (149-r, 50)),
    (3, D): (5, L, lambda r, c: (c+100, 49)),   # f
    (5, R): (3, U, lambda r, c: (149, r-100)),
    (1, U): (5, R, lambda r, c: (c+100, 0)),    # g
    (5, L): (1, D, lambda r, c: (0, r-100))
}

def next_pos(r, c, dir):
    nr, nc, ndir = r+directions[dir][0], c+directions[dir][1], dir
    if face_number(nr, nc) == None:
        _, ndir, xform = edges[(face_number(r, c), dir)]
        nr, nc = xform(r, c)
    if map[nr][nc] == WALL:
        return (r, c, dir)
    else:
        return (nr, nc, ndir)

solve()
