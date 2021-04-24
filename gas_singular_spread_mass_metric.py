import numpy 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
from matplotlib.colors import LogNorm
from velociraptor.tools.lines import binned_median_line as bml
import unyt

spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt')
mass = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_mass.txt')

fig, ax = pyplot.subplots(figsize = (20,20))

x_bins = numpy.logspace(numpy.log10(numpy.amin(mass)), numpy.log10(numpy.amax(mass)), num = 20)
y_bins = numpy.logspace(numpy.log10(numpy.amin(spread)), numpy.log10(numpy.amax(spread)), num = 20)
bins = numpy.logspace(numpy.log10(numpy.amin(mass)), numpy.log10(numpy.amax(mass)), num = 20)
h = ax.hist2d(mass, spread, bins = [x_bins, y_bins], norm = LogNorm())
pyplot.colorbar(h[3], ax=ax)
ax.loglog()
ax.set_ylabel('Spread metric [Mpc]')
ax.set_xlabel(r'Nearest halo mass [$M_{\odot}$]')
ax.tick_params(which = 'both', direction = 'in')
ax.tick_params(length = 10, width = 2)
bins = unyt.unyt_array(bins, units = 'msun')
spread = unyt.unyt_array(spread, units = 'Mpc')
mass = unyt.unyt_array(mass, units = 'msun')
centers, med, err = bml(mass, spread, x_bins = bins)
ax.plot(centers, med, linestyle = '--', linewidth = 7, color = 'red')
fig.savefig('/cosma5/data/durham/dc-murr1/gas_singular_spread_mass_metric.png')