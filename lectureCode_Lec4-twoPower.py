# From Lecture 4, How Environments Separate Variable Bindings

def square(x):
    return x*x

def twoPower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
        print x
        print n
    return x

x=3
y=4
z=8

if(max(x,y)==x):
    return x
elif (min(y,z)==z):
    return z
else:
    return y