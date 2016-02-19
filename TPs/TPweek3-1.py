def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    def frange(x, y, jump):
        r = start
        while r < stop:
       	    yield r
       	    r += step
       	    
    total = ()
    suma = 0
    for s in frange(start+1, stop, step):
        total += (f(s)*step,)
    for t in total:
        suma += t
    return suma