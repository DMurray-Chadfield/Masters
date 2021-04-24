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
snap = load('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5')
temp = snap.gas.temperatures

fig, ax = pyplot.subplots(figsize = (20,20))
x_bins = numpy.logspace(numpy.log10(numpy.amin(temp)), numpy.log10(numpy.amax(temp)), num = 100)
y_bins = numpy.logspace(numpy.log10(numpy.amin(spread)), numpy.log10(numpy.amax(spread)), num = 100)
h = ax.hist2d(temp, spread, bins = [x_bins, y_bins], norm = LogNorm())
pyplot.colorbar(h[3], ax=ax)
ax.loglog()
ax.set_ylabel('Spread metric [Mpc]')
ax.set_xlabel("Temperature [K]")
ax.tick_params(length = 10, width = 3)

x_bins = unyt.unyt_array(x_bins, units = temp.units)
spread = unyt.unyt_array(spread, units = 'Mpc')
centers, med, err = bml(temp, spread, x_bins = x_bins)
ax.plot(centers, med, linestyle = '--', linewidth = 7, color = 'red')

fig.savefig('/cosma5/data/durham/dc-murr1/gas_spread_temperature_metric.png')