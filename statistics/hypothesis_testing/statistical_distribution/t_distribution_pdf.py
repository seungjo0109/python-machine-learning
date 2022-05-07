from numpy import arange
from matplotlib import pyplot
from scipy.stats import t

sample_space = arange(-5, 5, 0.001)
dof = len(sample_space)-1

# calculate the probability distribution function
pdf = t.pdf(sample_space, dof)

# plot
pyplot.plot(sample_space, pdf)
pyplot.title("t-distribution pdf")
pyplot.show()