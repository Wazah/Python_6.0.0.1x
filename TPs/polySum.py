import math

def polysum(n, s):
    '''
    n is an int > 2(a polygon has 3 or more sides)
    s is a float for the length of each side
    returns area+(perimeter*perimeter) rounded to 4 decimal places
    '''
    if(n>2):
        area=(0.25*n*(s*s))/(math.tan(math.pi/n))
        perimeter=n*s
    else:
        print('Please enter a number > 2 for the number of sides(n)')
        return
    return round((area+(perimeter*perimeter)),4)
