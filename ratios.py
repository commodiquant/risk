import volatility
import numpy
import pandas

def sortino(rtns):
    # rtns is the period return expressed as a decimal
    # +0.53% = 0.0053
    std_down = numpy.sqrt(volatility.lpm(rtns, 0.0, 2))
    rtns = rtns + 1
    total_rtn = pandas.cumprod(rtns, axis=1)
    return total_rtn / std_down