# --- Day 17: Pyroclastic Flow ---
#
# Your handheld device has located an alternative exit from the cave
# for you and the elephants.  The ground is rumbling almost
# continuously now, but the strange valves bought you some time.  It's
# definitely getting warmer in here, though.
#
# The tunnels eventually open into a very tall, narrow chamber.
# Large, oddly-shaped rocks are falling into the chamber from above,
# presumably due to all the rumbling.  If you can't work out where the
# rocks will fall next, you might be crushed!
#
# The five types of rocks have the following peculiar shapes, where #
# is rock and . is empty space:
#
# ####
#
# .#.
# ###
# .#.
#
# ..#
# ..#
# ###
#
# #
# #
# #
# #
#
# ##
# ##
#
# The rocks fall in the order shown above: first the - shape, then the
# + shape, and so on.  Once the end of the list is reached, the same
# order repeats: the - shape falls first, sixth, 11th, 16th, etc.
#
# The rocks don't spin, but they do get pushed around by jets of hot
# gas coming out of the walls themselves.  A quick scan reveals the
# effect the jets of hot gas will have on the rocks as they fall (your
# puzzle input).
#
# For example, suppose this was the jet pattern in your cave:
#
# >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
#
# In jet patterns, < means a push to the left, while > means a push to
# the right.  The pattern above means that the jets will push a
# falling rock right, then right, then right, then left, then left,
# then right, and so on.  If the end of the list is reached, it
# repeats.
#
# The tall, vertical chamber is exactly seven units wide.  Each rock
# appears so that its left edge is two units away from the left wall
# and its bottom edge is three units above the highest rock in the
# room (or the floor, if there isn't one).
#
# After a rock appears, it alternates between being pushed by a jet of
# hot gas one unit (in the direction indicated by the next symbol in
# the jet pattern) and then falling one unit down.  If any movement
# would cause any part of the rock to move into the walls, floor, or a
# stopped rock, the movement instead does not occur.  If a downward
# movement would have caused a falling rock to move into the floor or
# an already-fallen rock, the falling rock stops where it is (having
# landed on something) and a new rock immediately begins falling.
#
# Drawing falling rocks with @ and stopped rocks with #, the jet
# pattern in the example above manifests as follows:
#
# The first rock begins falling:
# |..@@@@.|
# |.......|
# |.......|
# |.......|
# +-------+
#
# Jet of gas pushes rock right:
# |...@@@@|
# |.......|
# |.......|
# |.......|
# +-------+
#
# Rock falls 1 unit:
# |...@@@@|
# |.......|
# |.......|
# +-------+
#
# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# |.......|
# +-------+
#
# Rock falls 1 unit:
# |...@@@@|
# |.......|
# +-------+
#
# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# +-------+
#
# Rock falls 1 unit:
# |...@@@@|
# +-------+
#
# Jet of gas pushes rock left:
# |..@@@@.|
# +-------+
#
# Rock falls 1 unit, causing it to come to rest:
# |..####.|
# +-------+
#
# A new rock begins falling:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+
#
# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+
#
# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |..####.|
# +-------+
#
# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |..####.|
# +-------+
#
# Rock falls 1 unit:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |..####.|
# +-------+
#
# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |..####.|
# +-------+
#
# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |..####.|
# +-------+
#
# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |..####.|
# +-------+
#
# Rock falls 1 unit, causing it to come to rest:
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# A new rock begins falling:
# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# The moment each of the next few rocks begins falling, you would see
# this:
#
# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..#....|
# |..#....|
# |####...|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |..#....|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |.....#.|
# |.....#.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |....##.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |##..##.|
# |######.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
#
# To prove to the elephants your simulation is accurate, they want to
# know how tall the tower will get after 2022 rocks have stopped (but
# before the 2023rd rock begins falling).  In this example, the tower
# of rocks will be 3068 units tall.
#
# How many units tall will the tower of rocks be after 2022 rocks have
# stopped falling?

SHAPES = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],          # relative to
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],  # lower left corner
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

shape_index = 0
def next_shape():
    global shape_index
    v = SHAPES[shape_index]
    shape_index = (shape_index+1)%len(SHAPES)
    return v

jets = open("17.in").read().strip()

jet_index = 0
def next_jet():
    global jet_index
    v = jets[jet_index]
    jet_index = (jet_index+1)%len(jets)
    return v

W = 7  # chamber width

rock_coords = set()  # (r, c) coordinates of rock locations in chamber
max_r = 0  # row of highest rock

def is_rock(r, c):
    return r <= 0 or c < 0 or c >= W or (r, c) in rock_coords

def shape_fits(r, c, shape):
    # Return True if the shape fits at the given location.
    return not any(is_rock(r+dr, c+dc) for dr, dc in shape)

def place_shape(r, c, shape):
    global max_r
    for dr, dc in shape:
        rock_coords.add((r+dr, c+dc))
        max_r = max(max_r, r+dr)

def drop_next_shape():
    shape = next_shape()
    r, c = max_r+4, 2
    while True:
        if next_jet() == "<":
            if shape_fits(r, c-1, shape):
                c -= 1
        else:
            if shape_fits(r, c+1, shape):
                c += 1
        if shape_fits(r-1, c, shape):
            r -= 1
        else:
            break
    place_shape(r, c, shape)

for _ in range(2022):
    drop_next_shape()
print(max_r)

# --- Part Two ---
#
# The elephants are not impressed by your simulation.  They demand to
# know how tall the tower will be after 1000000000000 rocks have
# stopped!  Only then will they feel confident enough to proceed
# through the cave.
#
# In the example above, the tower would be 1514285714288 units tall!
#
# How tall will the tower be after 1000000000000 rocks have stopped?
#
# --------------------
#
# Such a tricky puzzle!  Clearly we need to look for a cycle.  The
# lengths of the shape and jet cycles are both prime, leading one to
# believe that the overall cycle length must be a multiple of 5*10091.
# Ah, but each shape uses up multiple (and varying) numbers of jets in
# each drop, with the miraculous net result that the overall cycle
# length is small, only 1745 in our case.  (How on Earth did Eric
# design this puzzle?)
#
# In looking for a cycle, the state of the puzzle consists of the
# shape and jet indices and the empty cells that are reachable from
# and below the row containing the highest rock (expressed in
# coordinates relative to the highest rock).  The latter quantity in
# effect captures the "appearance" of the chamber so far as it is
# relevant to future falling rocks.  The set of reachable empty cells
# is not a minimal expression of functional equivalence (not all
# reachable cells can be populated by shapes, for example), but it is
# sufficient.

from common import bfs, neighbors4

def reachable_empty_cells():
    s = set()
    def visit(node, prev, dist, accum, seen):
        r, c = node
        s.add((max_r-r, c))
        return [
            (nr, nc)
            for nr, nc in neighbors4(r, c, max_r+1, W)
            if not is_rock(nr, nc)
        ]
    for c in range(W):
        if not is_rock(max_r, c):
            bfs((max_r, c), visit)
    return s

rock_coords.clear()
max_r = 0
jet_index = shape_index = 0

seen_states = {}  # state => (drop number, height)
n = 0
while True:
    drop_next_shape()
    n += 1
    state = (tuple(sorted(reachable_empty_cells())), shape_index, jet_index)
    if state in seen_states:
        break
    seen_states[state] = (n, max_r)

offset = seen_states[state][0]  # number of drops to reach cycle start
offset_height = seen_states[state][1]  # height at cycle start
cycle_length = n-offset
cycle_height_incr = max_r-offset_height  # height increment each cycle
num_cycles, remainder = divmod(1000000000000-offset, cycle_length)

# The situation at this point:
#
#        /--------- num_cycles ---------\
# offset | cycle | cycle | .... | cycle | remainder |
#                ^ here now                         ^ 1000000000000
#
# We continue to drop an additional `remainder` rocks to bring us to
# this situation:
#
# offset | cycle | remainder |
#                            ^ after loop below
#
# At which point the current height is the answer after augmenting
# it with an additional num_cycles-1 cycles.

for _ in range(remainder):
    drop_next_shape()

print(max_r + (num_cycles-1)*cycle_height_incr)
