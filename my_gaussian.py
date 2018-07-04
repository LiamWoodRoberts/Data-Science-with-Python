## Gaussian

def my_gaussian(sigma,mu,start,end):
    '''returns x and y values for a gaussian distribution given:
    sigma = Full width half max / standard deviation
    mu = mean/centerpoint,
    start = start of range, end = end of range'''
    import numpy as np
    x = np.linspace(start,end,100)
    y = 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-mu)**2/(2*sigma**2))
    return x,y
