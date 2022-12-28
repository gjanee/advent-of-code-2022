# --- Day 24: Blizzard Basin ---
#
# With everything replanted for next year (and with elephants and
# monkeys to tend the grove), you and the Elves leave for the
# extraction point.
#
# Partway up the mountain that shields the grove is a flat, open area
# that serves as the extraction point.  It's a bit of a climb, but
# nothing the expedition can't handle.
#
# At least, that would normally be true; now that the mountain is
# covered in snow, things have become more difficult than the Elves
# are used to.
#
# As the expedition reaches a valley that must be traversed to reach
# the extraction site, you find that strong, turbulent winds are
# pushing small blizzards of snow and sharp ice around the valley.
# It's a good thing everyone packed warm clothes!  To make it across
# safely, you'll need to find a way to avoid them.
#
# Fortunately, it's easy to see all of this from the entrance to the
# valley, so you make a map of the valley and the blizzards (your
# puzzle input).  For example:
#
# #.#####
# #.....#
# #>....#
# #.....#
# #...v.#
# #.....#
# #####.#
#
# The walls of the valley are drawn as #; everything else is ground.
# Clear ground - where there is currently no blizzard - is drawn as ..
# Otherwise, blizzards are drawn with an arrow indicating their
# direction of motion: up (^), down (v), left (<), or right (>).
#
# The above map includes two blizzards, one moving right (>) and one
# moving down (v).  In one minute, each blizzard moves one position in
# the direction it is pointing:
#
# #.#####
# #.....#
# #.>...#
# #.....#
# #.....#
# #...v.#
# #####.#
#
# Due to conservation of blizzard energy, as a blizzard reaches the
# wall of the valley, a new blizzard forms on the opposite side of the
# valley moving in the same direction.  After another minute, the
# bottom downward-moving blizzard has been replaced with a new
# downward-moving blizzard at the top of the valley instead:
#
# #.#####
# #...v.#
# #..>..#
# #.....#
# #.....#
# #.....#
# #####.#
#
# Because blizzards are made of tiny snowflakes, they pass right
# through each other.  After another minute, both blizzards
# temporarily occupy the same position, marked 2:
#
# #.#####
# #.....#
# #...2.#
# #.....#
# #.....#
# #.....#
# #####.#
#
# After another minute, the situation resolves itself, giving each
# blizzard back its personal space:
#
# #.#####
# #.....#
# #....>#
# #...v.#
# #.....#
# #.....#
# #####.#
#
# Finally, after yet another minute, the rightward-facing blizzard on
# the right is replaced with a new one on the left facing the same
# direction:
#
# #.#####
# #.....#
# #>....#
# #.....#
# #...v.#
# #.....#
# #####.#
#
# This process repeats at least as long as you are observing it, but
# probably forever.
#
# Here is a more complex example:
#
# #.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#
#
# Your expedition begins in the only non-wall position in the top row
# and needs to reach the only non-wall position in the bottom row.  On
# each minute, you can move up, down, left, or right, or you can wait
# in place.  You and the blizzards act simultaneously, and you cannot
# share a position with a blizzard.
#
# In the above example, the fastest way to reach your goal requires 18
# steps.  Drawing the position of the expedition as E, one way to
# achieve this is:
#
# Initial state:
# #E######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#
#
# Minute 1, move down:
# #.######
# #E>3.<.#
# #<..<<.#
# #>2.22.#
# #>v..^<#
# ######.#
#
# Minute 2, move down:
# #.######
# #.2>2..#
# #E^22^<#
# #.>2.^>#
# #.>..<.#
# ######.#
#
# Minute 3, wait:
# #.######
# #<^<22.#
# #E2<.2.#
# #><2>..#
# #..><..#
# ######.#
#
# Minute 4, move up:
# #.######
# #E<..22#
# #<<.<..#
# #<2.>>.#
# #.^22^.#
# ######.#
#
# Minute 5, move right:
# #.######
# #2Ev.<>#
# #<.<..<#
# #.^>^22#
# #.2..2.#
# ######.#
#
# Minute 6, move right:
# #.######
# #>2E<.<#
# #.2v^2<#
# #>..>2>#
# #<....>#
# ######.#
#
# Minute 7, move down:
# #.######
# #.22^2.#
# #<vE<2.#
# #>>v<>.#
# #>....<#
# ######.#
#
# Minute 8, move left:
# #.######
# #.<>2^.#
# #.E<<.<#
# #.22..>#
# #.2v^2.#
# ######.#
#
# Minute 9, move up:
# #.######
# #<E2>>.#
# #.<<.<.#
# #>2>2^.#
# #.v><^.#
# ######.#
#
# Minute 10, move right:
# #.######
# #.2E.>2#
# #<2v2^.#
# #<>.>2.#
# #..<>..#
# ######.#
#
# Minute 11, wait:
# #.######
# #2^E^2>#
# #<v<.^<#
# #..2.>2#
# #.<..>.#
# ######.#
#
# Minute 12, move down:
# #.######
# #>>.<^<#
# #.<E.<<#
# #>v.><>#
# #<^v^^>#
# ######.#
#
# Minute 13, move down:
# #.######
# #.>3.<.#
# #<..<<.#
# #>2E22.#
# #>v..^<#
# ######.#
#
# Minute 14, move right:
# #.######
# #.2>2..#
# #.^22^<#
# #.>2E^>#
# #.>..<.#
# ######.#
#
# Minute 15, move right:
# #.######
# #<^<22.#
# #.2<.2.#
# #><2>E.#
# #..><..#
# ######.#
#
# Minute 16, move right:
# #.######
# #.<..22#
# #<<.<..#
# #<2.>>E#
# #.^22^.#
# ######.#
#
# Minute 17, move down:
# #.######
# #2.v.<>#
# #<.<..<#
# #.^>^22#
# #.2..2E#
# ######.#
#
# Minute 18, move down:
# #.######
# #>2.<.<#
# #.2v^2<#
# #>..>2>#
# #<....>#
# ######E#
#
# What is the fewest number of minutes required to avoid the blizzards
# and reach the goal?

from collections import namedtuple
from common import a_star, neighbors4

UP, DN, LT, RT = 0b0001, 0b0010, 0b0100, 0b1000  # directional bit masks
ON, WL = 0, 1  # open, wall

# Step 1.  Load the grid.

mapping = {"^": UP, "v": DN, "<": LT, ">": RT, ".": ON, "#": WL}

grid = [
    [mapping[c] for c in line.strip()]
    for line in open("24.in")
]
R, C = len(grid), len(grid[0])  # grid dimensions, including walls

# Step 2.  Determine the cycle of blizzard phases and open cell
# positions in each phase.  We will operate off this information, not
# the grid itself.

def advance_blizzards(grid):
    next_grid = [row.copy() for row in grid]
    for r in range(1, R-1):
        for c in range(1, C-1):
            next_grid[r][c] = ON
    def wrap_row(r):
        return (r-1)%(R-2)+1
    def wrap_col(c):
        return (c-1)%(C-2)+1
    for r in range(1, R-1):
        for c in range(1, C-1):
            if grid[r][c] & UP != 0:
                next_grid[wrap_row(r-1)][c] |= UP
            if grid[r][c] & DN != 0:
                next_grid[wrap_row(r+1)][c] |= DN
            if grid[r][c] & LT != 0:
                next_grid[r][wrap_col(c-1)] |= LT
            if grid[r][c] & RT != 0:
                next_grid[r][wrap_col(c+1)] |= RT
    return next_grid

open_cells = []  # sets of open cells, indexed by phase

while True:
    s = set((r, c) for r in range(R) for c in range(C) if grid[r][c] == ON)
    if len(open_cells) > 0 and s == open_cells[0]:
        break
    open_cells.append(s)
    grid = advance_blizzards(grid)

P = len(open_cells)  # blizzard phase cycle length

# Step 3.  Pathfinding.  A node in the search graph comprises a grid
# position and a blizzard phase.  There's a subtlety: we don't know
# what the blizzard phase will be when we arrive at the goal position,
# and hence all nodes with the same position as the goal, irrespective
# of blizzard phase, must test equal for A* to work.  This
# characteristic is needed only for the goal node.  For the start
# node, we can and must distinguish phases, as it happens that the
# shortest path requires that we wait at the start position for an
# opening.  We incorporate the goal position into nodes themselves.

class Node(namedtuple("Node_base", "r c p goal_r goal_c")):
    # The state of being at position (r, c) in blizzard phase `p` in
    # the context of goal position (goal_r, goal_c).

    @property
    def at_goal(self):
        return self.r == self.goal_r and self.c == self.goal_c

    def __eq__(self, other):
        return ((self.at_goal and other.at_goal) or super().__eq__(other))

    def __hash__(self):
        return hash((self.r, self.c))

def visit(node):
    l = []
    np = (node.p+1)%P
    for nr, nc in neighbors4(node.r, node.c, R, C):
        if (nr, nc) in open_cells[np]:
            l.append(Node(nr, nc, np, node.goal_r, node.goal_c))
    # Add the possibility of waiting.
    if (node.r, node.c) in open_cells[np]:
        l.append(Node(node.r, node.c, np, node.goal_r, node.goal_c))
    return [
        (n, 1, abs(n.goal_r-n.r)+abs(n.goal_c-n.c))
        for n in l
    ]

start = (0, grid[0].index(ON))
goal = (R-1, grid[R-1].index(ON))

path = a_star(
    Node(start[0], start[1], 0, goal[0], goal[1]),
    Node(goal[0], goal[1], 0, goal[0], goal[1]),
    visit
)

dist = len(path)-1
print(dist)

# --- Part Two ---
#
# As the expedition reaches the far side of the valley, one of the
# Elves looks especially dismayed:
#
# He forgot his snacks at the entrance to the valley!
#
# Since you're so good at dodging blizzards, the Elves humbly request
# that you go back for his snacks.  From the same initial conditions,
# how quickly can you make it from the start to the goal, then back to
# the start, then back to the goal?
#
# In the above example, the first trip to the goal takes 18 minutes,
# the trip back to the start takes 23 minutes, and the trip back to
# the goal again takes 13 minutes, for a total time of 54 minutes.
#
# What is the fewest number of minutes required to reach the goal, go
# back to the start, then reach the goal again?

path = a_star(
    Node(goal[0], goal[1], path[-1][0].p, start[0], start[1]),
    Node(start[0], start[1], 0, start[0], start[1]),
    visit
)
dist += len(path)-1

path = a_star(
    Node(start[0], start[1], path[-1][0].p, goal[0], goal[1]),
    Node(goal[0], goal[1], 0, goal[0], goal[1]),
    visit
)
dist += len(path)-1

print(dist)
