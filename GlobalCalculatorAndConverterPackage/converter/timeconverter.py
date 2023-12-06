def time_convert(time1, time2, value):
    conv = {
        's':1,
        'm':2,
        'h':3
    }
    
    sub=conv[time1]-conv[time2]
    if sub<0:
        return ("{:.3f}".format(value/(60**abs(sub))))
    else:
        return ("{:.3f}".format(value*(60**abs(sub))))