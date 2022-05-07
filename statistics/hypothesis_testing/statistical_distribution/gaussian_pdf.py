from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm

sample_space = arange(-5, 5, 0.001)
mean = 0.0
stdv = 1.0

# calculate the probability density function
pdf = norm.pdf(sample_space, mean, stdv)

# plot
pyplot.plot(sample_space, pdf)
pyplot.title("Gaussian probability distribution")
pyplot.show()