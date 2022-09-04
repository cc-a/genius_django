from collections import namedtuple
from statistics import mean, median, mode

Stats = namedtuple("stats", ("mean", "median", "mode"))


def calc_stats(data):
    """Calculate the mean, median and mode of `data`."""
    return Stats(mean(data), median(data), mode(data))
