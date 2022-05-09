from numpy import arange
from matplotlib import pyplot
from scipy.stats import chi2

sample_space = arange(0, 50, 0.01)
dof = 20

# calculate the Chi-Squared pdf
pdf = chi2.cdf(sample_space, dof)

# plot
pyplot.plot(sample_space, pdf)
pyplot.title("Chi-Squared cummulative density function")
pyplot.show()
