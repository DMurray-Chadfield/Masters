import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from scipy.interpolate import UnivariateSpline


dm_spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_spread.txt')
gas_spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt')

n_bins = 100

bins = numpy.linspace(numpy.min(dm_spread), numpy.max(dm_spread), n_bins)

p1, x1 = numpy.histogram(dm_spread, bins)
x1 = x1[:-1] + (x1[1] - x1[0])/2
f1 = UnivariateSpline(x1, p1, s=n_bins)

fig, (ax1, ax2) = pyplot.subplots(1,2)
ax1.hist(dm_spread, bins)
ax1.plot(x1, f1)
ax1.set_yscale('log')
ax1.set_xlabel('Dark Matter Spread Metric [Mpc]')
ax2.hist(gas_spread, bins)
ax2.set_yscale('log')
ax2.set_xlabel('Gas Spread Metric [Mpc]')
fig.savefig('/cosma5/data/durham/dc-murr1/spread_metric.png')