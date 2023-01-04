# --- Day 19: Not Enough Minerals ---
#
# Your scans show that the lava did indeed form obsidian!
#
# The wind has changed direction enough to stop sending lava droplets
# toward you, so you and the elephants exit the cave.  As you do, you
# notice a collection of geodes around the pond.  Perhaps you could
# use the obsidian to create some geode-cracking robots and break them
# open?
#
# To collect the obsidian from the bottom of the pond, you'll need
# waterproof obsidian-collecting robots.  Fortunately, there is an
# abundant amount of clay nearby that you can use to make them
# waterproof.
#
# In order to harvest the clay, you'll need special-purpose
# clay-collecting robots.  To make any type of robot, you'll need ore,
# which is also plentiful but in the opposite direction from the clay.
#
# Collecting ore requires ore-collecting robots with big drills.
# Fortunately, you have exactly one ore-collecting robot in your pack
# that you can use to kickstart the whole operation.
#
# Each robot can collect 1 of its resource type per minute.  It also
# takes one minute for the robot factory (also conveniently from your
# pack) to construct any type of robot, although it consumes the
# necessary resources available when construction begins.
#
# The robot factory has many blueprints (your puzzle input) you can
# choose from, but once you've configured it with a blueprint, you
# can't change it.  You'll need to work out which blueprint is best.
#
# For example:
#
# Blueprint 1:
#   Each ore robot costs 4 ore.
#   Each clay robot costs 2 ore.
#   Each obsidian robot costs 3 ore and 14 clay.
#   Each geode robot costs 2 ore and 7 obsidian.
#
# Blueprint 2:
#   Each ore robot costs 2 ore.
#   Each clay robot costs 3 ore.
#   Each obsidian robot costs 3 ore and 8 clay.
#   Each geode robot costs 3 ore and 12 obsidian.
#
# (Blueprints have been line-wrapped here for legibility.  The robot
# factory's actual assortment of blueprints are provided one blueprint
# per line.)
#
# The elephants are starting to look hungry, so you shouldn't take too
# long; you need to figure out which blueprint would maximize the
# number of opened geodes after 24 minutes by figuring out which
# robots to build and when to build them.
#
# Using blueprint 1 in the example above, the largest number of geodes
# you could open in 24 minutes is 9.  One way to achieve that is:
#
# == Minute 1 ==
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
#
# == Minute 2 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
#
# == Minute 3 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# The new clay-collecting robot is ready; you now have 1 of them.
#
# == Minute 4 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 1 clay-collecting robot collects 1 clay; you now have 1 clay.
#
# == Minute 5 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 1 clay-collecting robot collects 1 clay; you now have 2 clay.
# The new clay-collecting robot is ready; you now have 2 of them.
#
# == Minute 6 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 2 clay-collecting robots collect 2 clay; you now have 4 clay.
#
# == Minute 7 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 2 clay-collecting robots collect 2 clay; you now have 6 clay.
# The new clay-collecting robot is ready; you now have 3 of them.
#
# == Minute 8 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 3 clay-collecting robots collect 3 clay; you now have 9 clay.
#
# == Minute 9 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 3 clay-collecting robots collect 3 clay; you now have 12 clay.
#
# == Minute 10 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 3 clay-collecting robots collect 3 clay; you now have 15 clay.
#
# == Minute 11 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting
# robot.
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 3 clay-collecting robots collect 3 clay; you now have 4 clay.
# The new obsidian-collecting robot is ready; you now have 1 of them.
#
# == Minute 12 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 3 clay-collecting robots collect 3 clay; you now have 7 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 1
# obsidian.
# The new clay-collecting robot is ready; you now have 4 of them.
#
# == Minute 13 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 11 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 2
# obsidian.
#
# == Minute 14 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 15 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 3
# obsidian.
#
# == Minute 15 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting
# robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 4 clay-collecting robots collect 4 clay; you now have 5 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 4
# obsidian.
# The new obsidian-collecting robot is ready; you now have 2 of them.
#
# == Minute 16 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 9 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 6
# obsidian.
#
# == Minute 17 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 13 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 8
# obsidian.
#
# == Minute 18 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 17 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 3
# obsidian.
# The new geode-cracking robot is ready; you now have 1 of them.
#
# == Minute 19 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 21 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 5
# obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
#
# == Minute 20 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 4 clay-collecting robots collect 4 clay; you now have 25 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 7
# obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
#
# == Minute 21 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 29 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 2
# obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
# The new geode-cracking robot is ready; you now have 2 of them.
#
# == Minute 22 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 4 clay-collecting robots collect 4 clay; you now have 33 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 4
# obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.
#
# == Minute 23 ==
# 1 ore-collecting robot collects 1 ore; you now have 5 ore.
# 4 clay-collecting robots collect 4 clay; you now have 37 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 6
# obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.
#
# == Minute 24 ==
# 1 ore-collecting robot collects 1 ore; you now have 6 ore.
# 4 clay-collecting robots collect 4 clay; you now have 41 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 8
# obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.
#
# However, by using blueprint 2 in the example above, you could do
# even better: the largest number of geodes you could open in 24
# minutes is 12.
#
# Determine the quality level of each blueprint by multiplying that
# blueprint's ID number with the largest number of geodes that can be
# opened in 24 minutes using that blueprint.  In this example, the
# first blueprint has ID 1 and can open 9 geodes, so its quality level
# is 9.  The second blueprint has ID 2 and can open 12 geodes, so its
# quality level is 24.  Finally, if you add up the quality levels of
# all of the blueprints in the list, you get 33.
#
# Determine the quality level of each blueprint using the largest
# number of geodes it could produce in 24 minutes.  What do you get if
# you add up the quality level of all of the blueprints in your list?
#
# --------------------
#
# Difficult puzzle!  We explore the tree of all possible solutions,
# but prune branches that can be proven to be unprofitable.  The
# pruning rules are very specific to this puzzle and took a fair
# amount of experimentation to discover and articulate; they're
# documented in the code below.
#
# That at most one robot can be created in any given minute makes this
# quite an odd puzzle.  An implication is that if at most N units of a
# type of resource are required to build any type of robot, then there
# will never be a need for more than N robots of that type since the
# excess resources can never be utilized.  Further, once created, N
# robots will continue to produce N resources every minute.  This can
# lead to quadratic growth if sufficient resources allow a new robot
# to be created every minute.

import re

R, C, O, G = range(4)  # ore, clay, obsidian, geode
W = -1  # wait

# It will be convenient to think of ourselves as working in a
# 4-dimensional vector space in which axes correspond to resource
# types and values indicate numbers of resources or robots, but with a
# peculiar kind of ordering.

class Quartet(tuple):
    # (R, C, O, G)

    def __new__(cls, *args):
        return super().__new__(cls, args)

    def __add__(self, other):
        return Quartet(
            self[R]+other[R],
            self[C]+other[C],
            self[O]+other[O],
            self[G]+other[G]
        )

    def __sub__(self, other):
        return Quartet(
            self[R]-other[R],
            self[C]-other[C],
            self[O]-other[O],
            self[G]-other[G]
        )

    def __le__(self, other):
        return (
            self[R] <= other[R]
            and self[C] <= other[C]
            and self[O] <= other[O]
            and self[G] <= other[G]
        )

zero = Quartet(0, 0, 0, 0)

def one(type):
    v = [0, 0, 0, 0]
    v[type] = 1
    return Quartet(*v)

def walk(
    blueprint,
    max_robots,
    robots,
    holdings,
    prev_holdings,
    last_action,
    time,
    limit
):
    new_holdings = holdings + robots  # holdings after this minute elapses
    if time == limit:
        return new_holdings[G]
    lacking_resources = False
    max_geodes = 0
    for r in [R, C, O, G]:  # try building another robot
        # Abandon if we don't have enough resources to build the
        # robot.
        if not (blueprint[r] <= holdings):
            lacking_resources = True
            continue
        # Prune if, in the previous round, we could have built a robot
        # of this type but chose to wait instead.  The idea being that
        # if there is value in building this type of robot, the value
        # could already have been realized by building it in the
        # previous round; nothing is gained by waiting.  Put another
        # way, if we imagine that a robot must be built within a
        # certain window, this forces that we consider building the
        # robot only at the (single) earliest opportunity.  Note,
        # though, that building any type of robot in the previous
        # round, even of a different type, resets this condition.
        if last_action == W and blueprint[r] <= prev_holdings:
            continue
        # Prune if, for resource types other than geode, we already
        # have enough resources and robots of this type to satisfy any
        # future need.  This rule started out expressed in terms of
        # number of robots: prune if robots[r] >= max_robots[r].  But
        # phrasing the way below, in terms of number of resources,
        # allows us to incorporate the effect of the current holdings.
        t = limit-time
        if r != G and new_holdings[r]+robots[r]*t >= max_robots[r]*t:
            continue
        # Passed all pruning checks; build the robot.
        max_geodes = max(
            max_geodes,
            walk(
                blueprint,
                max_robots,
                robots + one(r),
                new_holdings - blueprint[r],
                holdings,
                r,
                time+1,
                limit
            )
        )
    if lacking_resources:  # try waiting
        max_geodes = max(
            max_geodes,
            walk(
                blueprint,
                max_robots,
                robots,
                new_holdings,
                holdings,
                W,
                time+1,
                limit
            )
        )
    return max_geodes

def blueprints():
    for line in open("19.in"):
        id, r_r_cost, c_r_cost, o_r_cost, o_c_cost, g_r_cost, g_o_cost = (
            int(v) for v in re.findall("\d+", line)
        )
        blueprint = [
            Quartet(r_r_cost, 0,        0,        0),  # R
            Quartet(c_r_cost, 0,        0,        0),  # C
            Quartet(o_r_cost, o_c_cost, 0,        0),  # O
            Quartet(g_r_cost, 0,        g_o_cost, 0)   # G
        ]
        max_robots = Quartet(
            max(q[R] for q in blueprint),
            max(q[C] for q in blueprint),
            max(q[O] for q in blueprint),
            max(q[G] for q in blueprint)
        )
        yield id, blueprint, max_robots

print(
    sum(
        id * walk(blueprint, max_robots, one(R), zero, zero, W, 1, 24)
        for id, blueprint, max_robots in blueprints()
    )
)

# --- Part Two ---
#
# While you were choosing the best blueprint, the elephants found some
# food on their own, so you're not in as much of a hurry; you figure
# you probably have 32 minutes before the wind changes direction again
# and you'll need to get out of range of the erupting volcano.
#
# Unfortunately, one of the elephants ate most of your blueprint list!
# Now, only the first three blueprints in your list are intact.
#
# In 32 minutes, the largest number of geodes blueprint 1 (from the
# example above) can open is 56.  One way to achieve that is:
#
# == Minute 1 ==
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
#
# == Minute 2 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
#
# == Minute 3 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
#
# == Minute 4 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
#
# == Minute 5 ==
# Spend 4 ore to start building an ore-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# The new ore-collecting robot is ready; you now have 2 of them.
#
# == Minute 6 ==
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
#
# == Minute 7 ==
# Spend 2 ore to start building a clay-collecting robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# The new clay-collecting robot is ready; you now have 1 of them.
#
# == Minute 8 ==
# Spend 2 ore to start building a clay-collecting robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 1 clay-collecting robot collects 1 clay; you now have 1 clay.
# The new clay-collecting robot is ready; you now have 2 of them.
#
# == Minute 9 ==
# Spend 2 ore to start building a clay-collecting robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 2 clay-collecting robots collect 2 clay; you now have 3 clay.
# The new clay-collecting robot is ready; you now have 3 of them.
#
# == Minute 10 ==
# Spend 2 ore to start building a clay-collecting robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 3 clay-collecting robots collect 3 clay; you now have 6 clay.
# The new clay-collecting robot is ready; you now have 4 of them.
#
# == Minute 11 ==
# Spend 2 ore to start building a clay-collecting robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 10 clay.
# The new clay-collecting robot is ready; you now have 5 of them.
#
# == Minute 12 ==
# Spend 2 ore to start building a clay-collecting robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 5 clay-collecting robots collect 5 clay; you now have 15 clay.
# The new clay-collecting robot is ready; you now have 6 of them.
#
# == Minute 13 ==
# Spend 2 ore to start building a clay-collecting robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 6 clay-collecting robots collect 6 clay; you now have 21 clay.
# The new clay-collecting robot is ready; you now have 7 of them.
#
# == Minute 14 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting
# robot.
# 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# The new obsidian-collecting robot is ready; you now have 1 of them.
#
# == Minute 15 ==
# 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# 7 clay-collecting robots collect 7 clay; you now have 21 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 1
# obsidian.
#
# == Minute 16 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting
# robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 2
# obsidian.
# The new obsidian-collecting robot is ready; you now have 2 of them.
#
# == Minute 17 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting
# robot.
# 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# 7 clay-collecting robots collect 7 clay; you now have 7 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 4
# obsidian.
# The new obsidian-collecting robot is ready; you now have 3 of them.
#
# == Minute 18 ==
# 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# 3 obsidian-collecting robots collect 3 obsidian; you now have 7
# obsidian.
#
# == Minute 19 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting
# robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 7 clay-collecting robots collect 7 clay; you now have 7 clay.
# 3 obsidian-collecting robots collect 3 obsidian; you now have 10
# obsidian.
# The new obsidian-collecting robot is ready; you now have 4 of them.
#
# == Minute 20 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# 4 obsidian-collecting robots collect 4 obsidian; you now have 7
# obsidian.
# The new geode-cracking robot is ready; you now have 1 of them.
#
# == Minute 21 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting
# robot.
# 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# 7 clay-collecting robots collect 7 clay; you now have 7 clay.
# 4 obsidian-collecting robots collect 4 obsidian; you now have 11
# obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
# The new obsidian-collecting robot is ready; you now have 5 of them.
#
# == Minute 22 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 9
# obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
# The new geode-cracking robot is ready; you now have 2 of them.
#
# == Minute 23 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# 7 clay-collecting robots collect 7 clay; you now have 21 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 7
# obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 4 open geodes.
# The new geode-cracking robot is ready; you now have 3 of them.
#
# == Minute 24 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# 7 clay-collecting robots collect 7 clay; you now have 28 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 5
# obsidian.
# 3 geode-cracking robots crack 3 geodes; you now have 7 open geodes.
# The new geode-cracking robot is ready; you now have 4 of them.
#
# == Minute 25 ==
# 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# 7 clay-collecting robots collect 7 clay; you now have 35 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 10
# obsidian.
# 4 geode-cracking robots crack 4 geodes; you now have 11 open geodes.
#
# == Minute 26 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# 7 clay-collecting robots collect 7 clay; you now have 42 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 8
# obsidian.
# 4 geode-cracking robots crack 4 geodes; you now have 15 open geodes.
# The new geode-cracking robot is ready; you now have 5 of them.
#
# == Minute 27 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# 7 clay-collecting robots collect 7 clay; you now have 49 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 6
# obsidian.
# 5 geode-cracking robots crack 5 geodes; you now have 20 open geodes.
# The new geode-cracking robot is ready; you now have 6 of them.
#
# == Minute 28 ==
# 2 ore-collecting robots collect 2 ore; you now have 6 ore.
# 7 clay-collecting robots collect 7 clay; you now have 56 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 11
# obsidian.
# 6 geode-cracking robots crack 6 geodes; you now have 26 open geodes.
#
# == Minute 29 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 6 ore.
# 7 clay-collecting robots collect 7 clay; you now have 63 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 9
# obsidian.
# 6 geode-cracking robots crack 6 geodes; you now have 32 open geodes.
# The new geode-cracking robot is ready; you now have 7 of them.
#
# == Minute 30 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 6 ore.
# 7 clay-collecting robots collect 7 clay; you now have 70 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 7
# obsidian.
# 7 geode-cracking robots crack 7 geodes; you now have 39 open geodes.
# The new geode-cracking robot is ready; you now have 8 of them.
#
# == Minute 31 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 2 ore-collecting robots collect 2 ore; you now have 6 ore.
# 7 clay-collecting robots collect 7 clay; you now have 77 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 5
# obsidian.
# 8 geode-cracking robots crack 8 geodes; you now have 47 open geodes.
# The new geode-cracking robot is ready; you now have 9 of them.
#
# == Minute 32 ==
# 2 ore-collecting robots collect 2 ore; you now have 8 ore.
# 7 clay-collecting robots collect 7 clay; you now have 84 clay.
# 5 obsidian-collecting robots collect 5 obsidian; you now have 10
# obsidian.
# 9 geode-cracking robots crack 9 geodes; you now have 56 open geodes.
#
# However, blueprint 2 from the example above is still better; using
# it, the largest number of geodes you could open in 32 minutes is 62.
#
# You no longer have enough blueprints to worry about quality levels.
# Instead, for each of the first three blueprints, determine the
# largest number of geodes you could open; then, multiply these three
# values together.
#
# Don't worry about quality levels; instead, just determine the
# largest number of geodes you could open using each of the first
# three blueprints.  What do you get if you multiply these numbers
# together?

from itertools import islice
from math import prod

print(
    prod(
        walk(blueprint, max_robots, one(R), zero, zero, W, 1, 32)
        for id, blueprint, max_robots in islice(blueprints(), 3)
    )
)
