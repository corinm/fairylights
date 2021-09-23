from line_profiler import LineProfiler
from colour import Color

from patterns.twinkle.Twinkle import Twinkle

lp = LineProfiler()

def main():
    t = Twinkle(150, [Color('red'), Color('blue', Color('green'))])
    t.tick()
    lp_wrapper = lp(t.tick)
    lp_wrapper()
    lp.print_stats()

main()