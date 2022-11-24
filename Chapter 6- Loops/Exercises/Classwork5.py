# less 2.0
def numzero(x):
    if (x==0):
        return
    print(x)
    x=x-1
    numzero(x)
numzero(12)