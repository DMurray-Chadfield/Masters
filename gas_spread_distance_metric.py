import numpy 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
from matplotlib.colors import LogNorm
from swiftsimio import load
from velociraptor.tools.lines import binned_median_line as bml
import unyt

spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt')
distance = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_distance.txt')
snap = load('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5')

fig, ax = pyplot.subplots(figsize = (20,20))
x_bins = numpy.logspace(numpy.log10(numpy.amin(distance)), numpy.log10(numpy.amax(distance)), num = 100)
bins = numpy.logspace(numpy.log10(numpy.amin(distance)), numpy.log10(numpy.amax(distance)), num = 20)
y_bins = numpy.logspace(numpy.log10(numpy.amin(spread)), numpy.log10(numpy.amax(spread)), num = 100)
h = ax.hist2d(distance, spread, bins = [x_bins, y_bins], norm = LogNorm())
pyplot.colorbar(h[3], ax=ax)
ax.loglog()
ax.set_ylabel('Spread metric [Mpc]')
ax.set_xlabel("Distance to nearest halo [Mpc]")
ax.tick_params(which = 'both', direction = 'in')
ax.tick_params(length = 10, width = 2)
bins = unyt.unyt_array(bins, units = 'Mpc')
spread = unyt.unyt_array(spread, units = 'Mpc')
distance = unyt.unyt_array(distance, units = 'Mpc')
centers, med, err = bml(distance, spread, x_bins = bins)
ax.plot(centers, med, linestyle = '--', linewidth = 7, color = 'red')

fig.savefig('/cosma5/data/durham/dc-murr1/gas_spread_distance_metric.png')