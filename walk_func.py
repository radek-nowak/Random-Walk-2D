import numpy as np


N = 500 #number of steps

def walk_gauss(steps):
    '''
    Simulates random walk in 2D. Length of a step is modulus of a variable from GAUSSIAN distribution.

    Args:
        steps: int - number of steps in a walk
    Returns:
        xs,ys: array of float64 - two arrays (coordinates for each step)
        np.sqrt(x**2 + y**2): float64 - distance between first and last coordinate
    '''
    xs = np.zeros(steps)
    ys = np.zeros(steps)
    x,y = 0,0
    for step in range(steps):
        theta = np.random.uniform(0,2*np.pi)
        r = abs(np.random.normal(0,1))
        xs[step] = xs[step-1] + np.cos(theta)*r
        ys[step] = ys[step-1] + np.sin(theta)*r
        x += np.cos(theta)*r
        y += np.sin(theta)*r
    return (xs,ys,np.sqrt(x**2 + y**2))



def walk_cauchy(steps):
    '''
    Simulates random walk in 2D. Length of a step is modulus of a variable from CAUCHY distribution.

    Args:
        steps: int - number of steps in a walk
    Returns:
        xs,ys: array of float64 - two arrays (coordinates for each step)
        np.sqrt(x**2 + y**2): float64 - distance between first and last coordinate
    '''
    xs = np.zeros(steps)
    ys = np.zeros(steps)
    x,y = 0,0
    for step in range(steps):
        theta = np.random.uniform(0,2*np.pi)
        r = abs(np.random.standard_cauchy())
        xs[step] = xs[step-1] + np.cos(theta)*r
        ys[step] = ys[step-1] + np.sin(theta)*r
        x += np.cos(theta)*r
        y += np.sin(theta)*r
    return (xs,ys,np.sqrt(x**2 + y**2))


