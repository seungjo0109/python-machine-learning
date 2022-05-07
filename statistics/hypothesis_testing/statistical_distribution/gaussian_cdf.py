from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm

sample_space = arange(-5, 5, 0.001)

# calculate the cummulative distribution function
cdf = norm.cdf(sample_space)

# plot
pyplot.plot(sample_space, cdf)
pyplot.title("Gaussian cummulative distribution")
pyplot.show()