from line_profiler import LineProfiler
from colour import Color

from effects.twinkle.Twinkle import Twinkle
from effects.twinkle.TwinkleBulb import TwinkleBulb

lp = LineProfiler()

def main():
    t = Twinkle(1000, [Color('red'), Color('blue', Color('green'))])
    lp_wrapper = lp(t.tick)
    lp_wrapper()
    lp.print_stats()

# def main():
#     t = TwinkleBulb(0.8, 0.2)
#     t.setColourAtPeak(Color('red'))
#     lp_wrapper = lp(t.incrementTimeDelta)
#     lp_wrapper(0.004)
#     lp.print_stats()

main()