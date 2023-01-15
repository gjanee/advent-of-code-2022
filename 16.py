# --- Day 16: Proboscidea Volcanium ---
#
# The sensors have led you to the origin of the distress signal: yet
# another handheld device, just like the one the Elves gave you.
# However, you don't see any Elves around; instead, the device is
# surrounded by elephants!  They must have gotten lost in these
# tunnels, and one of the elephants apparently figured out how to turn
# on the distress signal.
#
# The ground rumbles again, much stronger this time.  What kind of
# cave is this, exactly?  You scan the cave with your handheld device;
# it reports mostly igneous rock, some ash, pockets of pressurized
# gas, magma... this isn't just a cave, it's a volcano!
#
# You need to get the elephants out of here, quickly.  Your device
# estimates that you have 30 minutes before the volcano erupts, so you
# don't have time to go back out the way you came in.
#
# You scan the cave for other options and discover a network of pipes
# and pressure-release valves.  You aren't sure how such a system got
# into a volcano, but you don't have time to complain; your device
# produces a report (your puzzle input) of each valve's flow rate if
# it were opened (in pressure per minute) and the tunnels you could
# use to move between the valves.
#
# There's even a valve in the room you and the elephants are currently
# standing in labeled AA.  You estimate it will take you one minute to
# open a single valve and one minute to follow any tunnel from one
# valve to another.  What is the most pressure you could release?
#
# For example, suppose you had the following scan output:
#
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II
#
# All of the valves begin closed.  You start at valve AA, but it must
# be damaged or jammed or something: its flow rate is 0, so there's no
# point in opening it.  However, you could spend one minute moving to
# valve BB and another minute opening it; doing so would release
# pressure during the remaining 28 minutes at a flow rate of 13, a
# total eventual pressure release of 28 * 13 = 364.  Then, you could
# spend your third minute moving to valve CC and your fourth minute
# opening it, providing an additional 26 minutes of eventual pressure
# release at a flow rate of 2, or 52 total pressure released by valve
# CC.
#
# Making your way through the tunnels like this, you could probably
# open many or all of the valves by the time 30 minutes have elapsed.
# However, you need to release as much pressure as possible, so you'll
# need to be methodical.  Instead, consider this approach:
#
# == Minute 1 ==
# No valves are open.
# You move to valve DD.
#
# == Minute 2 ==
# No valves are open.
# You open valve DD.
#
# == Minute 3 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve CC.
#
# == Minute 4 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve BB.
#
# == Minute 5 ==
# Valve DD is open, releasing 20 pressure.
# You open valve BB.
#
# == Minute 6 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve AA.
#
# == Minute 7 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve II.
#
# == Minute 8 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve JJ.
#
# == Minute 9 ==
# Valves BB and DD are open, releasing 33 pressure.
# You open valve JJ.
#
# == Minute 10 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve II.
#
# == Minute 11 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve AA.
#
# == Minute 12 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve DD.
#
# == Minute 13 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve EE.
#
# == Minute 14 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve FF.
#
# == Minute 15 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve GG.
#
# == Minute 16 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve HH.
#
# == Minute 17 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You open valve HH.
#
# == Minute 18 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve GG.
#
# == Minute 19 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve FF.
#
# == Minute 20 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve EE.
#
# == Minute 21 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You open valve EE.
#
# == Minute 22 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve DD.
#
# == Minute 23 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve CC.
#
# == Minute 24 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You open valve CC.
#
# == Minute 25 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# == Minute 26 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# == Minute 27 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# == Minute 28 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# == Minute 29 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# == Minute 30 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# This approach lets you release the most pressure possible in 30
# minutes with this valve layout, 1651.
#
# Work out the steps to release the most pressure in 30 minutes.  What
# is the most pressure you can release?
#
# --------------------
#
# Most difficult puzzle of the year.  The graph aspect is dispensed
# with by noticing that all that matters is which valves (that have
# positive flow rate, that is) are opened in which order (but of
# course we must move between valves as quickly as possible).  Thus we
# pre-compute all shortest paths between valves and then use depth
# first search to examine all possible orderings of valves.  This
# works fine for part 1, but for part 2 we will have to repeat this
# process thousands of times.  We explored many optimizations such as
# pruning, memoization, and using bitmasks, but that got the runtime
# down to only 20 seconds.  Instead, the real optimization (obvious in
# hindsight, as always) is to keep track of the maximum flow rate
# achieved for each possible set of valves when starting from valve AA
# at minute 0, as will be described further under part 2 below.

from collections import defaultdict
from common import fw
import re

flow_rate = {}
graph = defaultdict(lambda: [])

for line in open("16.in"):
    m = re.findall("\d+|[A-Z][A-Z]", line)
    flow_rate[m[0]] = int(m[1])
    graph[m[0]] = m[2:]

distances = fw(
    {node: [(n, 1) for n in edges] for node, edges in graph.items()}
)

def walk(valve, seen, todo, time, flow, best):
    # valve: the valve being visited (not yet opened)
    # seen: set of valves already open
    # todo: set of remaining valves (not including `valve`)
    # time: time remaining
    # flow: total flow rate achieved so far
    # best: mapping set of valves => maximum flow rate achieved
    flow += flow_rate[valve]*time
    if valve != "AA":
        seen.add(valve)
    fseen = frozenset(seen)
    best[fseen] = max(best.get(fseen, 0), flow)
    max_flow = flow
    for v in list(todo):
        time_to_open = distances[(valve, v)]+1
        if time_to_open < time:
            todo.remove(v)
            max_flow = max(
                max_flow,
                walk(v, seen, todo, time-time_to_open, flow, best)
            )
            todo.add(v)
    seen.discard(valve)
    return max_flow

valves = set(valve for valve, rate in flow_rate.items() if rate > 0)
print(walk("AA", set(), valves, 30, 0, {}))

# --- Part Two ---
#
# You're worried that even with an optimal approach, the pressure
# released won't be enough.  What if you got one of the elephants to
# help you?
#
# It would take you 4 minutes to teach an elephant how to open the
# right valves in the right order, leaving you with only 26 minutes to
# actually execute your plan.  Would having two of you working
# together be better, even if it means having less time?  (Assume that
# you teach the elephant before opening any valves yourself, giving
# you both the same full 26 minutes.)
#
# In the example above, you could teach the elephant to help you as
# follows:
#
# == Minute 1 ==
# No valves are open.
# You move to valve II.
# The elephant moves to valve DD.
#
# == Minute 2 ==
# No valves are open.
# You move to valve JJ.
# The elephant opens valve DD.
#
# == Minute 3 ==
# Valve DD is open, releasing 20 pressure.
# You open valve JJ.
# The elephant moves to valve EE.
#
# == Minute 4 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve II.
# The elephant moves to valve FF.
#
# == Minute 5 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve AA.
# The elephant moves to valve GG.
#
# == Minute 6 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve BB.
# The elephant moves to valve HH.
#
# == Minute 7 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You open valve BB.
# The elephant opens valve HH.
#
# == Minute 8 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve CC.
# The elephant moves to valve GG.
#
# == Minute 9 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You open valve CC.
# The elephant moves to valve FF.
#
# == Minute 10 ==
# Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
# The elephant moves to valve EE.
#
# == Minute 11 ==
# Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
# The elephant opens valve EE.
#
# (At this point, all valves are open.)
#
# == Minute 12 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# ...
#
# == Minute 20 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# ...
#
# == Minute 26 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# With the elephant helping, after 26 minutes, the best you could do
# would release a total of 1707 pressure.
#
# With you and an elephant working together for 26 minutes, what is
# the most pressure you could release?
#
# --------------------
#
# Valves can't be opened more than once, so we look at all ways of
# partitioning the valves between ourselves and the elephant.  Here
# the creation of the `best` mapping pays off handsomely, for it
# answers exactly what we want to know for a given partition--- and
# `best` need be computed only once.  Notice how we are relying on the
# fact that both we and the elephant start from valve AA at time 0.
#
# It turns out that out of all possible partitions, only a fraction
# are reachable due to the reduced time limit.  Reachable valve
# subsets correspond to those in `best`.

best = {}
walk("AA", set(), valves, 26, 0, best)

print(
    max(
        best[a]+best[b]
        for a in best
        for b in best
        if a.isdisjoint(b)
    )
)
