# --- Day 18: Boiling Boulders ---
#
# You and the elephants finally reach fresh air.  You've emerged near
# the base of a large volcano that seems to be actively erupting!
# Fortunately, the lava seems to be flowing away from you and toward
# the ocean.
#
# Bits of lava are still being ejected toward you, so you're
# sheltering in the cavern exit a little longer.  Outside the cave,
# you can see the lava landing in a pond and hear it loudly hissing as
# it solidifies.
#
# Depending on the specific compounds in the lava and speed at which
# it cools, it might be forming obsidian!  The cooling rate should be
# based on the surface area of the lava droplets, so you take a quick
# scan of a droplet as it flies past you (your puzzle input).
#
# Because of how quickly the lava is moving, the scan isn't very good;
# its resolution is quite low and, as a result, it approximates the
# shape of the lava droplet with 1x1x1 cubes on a 3D grid, each given
# as its x,y,z position.
#
# To approximate the surface area, count the number of sides of each
# cube that are not immediately connected to another cube.  So, if
# your scan were only two adjacent cubes like 1,1,1 and 2,1,1, each
# cube would have a single side covered and five sides exposed, a
# total surface area of 10 sides.
#
# Here's a larger example:
#
# 2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5
#
# In the above example, after counting up all the sides that aren't
# connected to another cube, the total surface area is 64.
#
# What is the surface area of your scanned lava droplet?

cubes = {
    tuple(int(v) for v in line.split(","))
    for line in open("18.in")
}

deltas = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def surface_area(cubes):
    return sum(
        (x+dx, y+dy, z+dz) not in cubes
        for x, y, z in cubes
        for dx, dy, dz in deltas
    )

print(surface_area(cubes))

# --- Part Two ---
#
# Something seems off about your calculation.  The cooling rate
# depends on exterior surface area, but your calculation also included
# the surface area of air pockets trapped in the lava droplet.
#
# Instead, consider only cube sides that could be reached by the water
# and steam as the lava droplet tumbles into the pond.  The steam will
# expand to reach as much as possible, completely displacing any air
# on the outside of the lava droplet but never expanding diagonally.
#
# In the larger example above, exactly one cube of air is trapped
# within the lava droplet (at 2,2,5), so the exterior surface area of
# the lava droplet is 58.
#
# What is the exterior surface area of your scanned lava droplet?
#
# --------------------
#
# We thought of several scanline approaches, but the logic is hard to
# get right amid the many edge cases, particularly if the droplet is
# concave in places and if trapped air pockets contain further lava as
# is the case with our input.  Instead, we take a cue from the puzzle
# and place the droplet inside a box of water one cell wider than the
# droplet in each direction.  The exterior surface area of the droplet
# is just the surface area of the water less the water's (easy to
# compute) exterior surface area.

from common import minmax, bfs

xmin, xmax = minmax(x for x, y, z in cubes)
ymin, ymax = minmax(y for x, y, z in cubes)
zmin, zmax = minmax(z for x, y, z in cubes)

# box dimensions
xlength, ylength, zlength = xmax-xmin+3, ymax-ymin+3, zmax-zmin+3

water = set()  # coordinates of cubes outside the droplet

def visit(node, prev, dist, accum, seen):
    water.add(node)
    x, y, z = node
    return [
        (x+dx, y+dy, z+dz)
        for dx, dy, dz in deltas
        if (
            x+dx in range(xmin-1, xmax+2)
            and y+dy in range(ymin-1, ymax+2)
            and z+dz in range(zmin-1, zmax+2)
            and (x+dx, y+dy, z+dz) not in cubes
        )
    ]

bfs((xmin-1, ymin-1, zmin-1), visit)

print(
    surface_area(water)
    - 2*(xlength*ylength + ylength*zlength + zlength*xlength)
)
