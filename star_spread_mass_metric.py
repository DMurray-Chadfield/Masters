import numpy 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
from matplotlib.colors import LogNorm

spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/star_spread.txt')
mass = numpy.loadtxt('/cosma5/data/durham/dc-murr1/star_average_halo_mass.txt')

fig, ax = pyplot.subplots(figsize = (20,20))
x_bins = numpy.logspace(numpy.log10(numpy.amin(mass)), numpy.log10(numpy.amax(mass)), num = 100)
y_bins = numpy.logspace(numpy.log10(numpy.amin(spread)), numpy.log10(numpy.amax(spread)), num = 100)
h = ax.hist2d(mass, spread, bins = [x_bins, y_bins], norm = LogNorm())
pyplot.colorbar(h[3], ax=ax)
ax.loglog()
ax.set_ylabel('Spread metric [Mpc]')
ax.set_xlabel(r'Mass [$M_{\odot}$]')
fig.savefig('/cosma5/data/durham/dc-murr1/star_spread_mass_metric.png')