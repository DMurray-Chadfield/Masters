import numpy 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
import unyt
from velociraptor.tools.lines import binned_median_line as bml

spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_spread.txt')
mass = numpy.loadtxt('/cosma5/data/durham/dc-murr1/average_halo_mass.txt')
radius = numpy.loadtxt('/cosma5/data/durham/dc-murr1/average_halo_radius.txt')

mass_bins = numpy.logspace(numpy.log10(numpy.min(mass)), numpy.log10(numpy.max(mass)), 20)
mass_bins = unyt.unyt_array(mass_bins, units = unyt.msun)
mass = unyt.unyt_array(mass, units = unyt.msun)
spread = unyt.unyt_array(spread, units = unyt.Mpc)
radius = unyt.unyt_array(radius, units = unyt.Mpc)
centers, med, err = bml(mass, spread, mass_bins, minimum_in_bin = 1)
rad_centers, rad_med, rad_err = bml(mass, 2*radius, mass_bins, minimum_in_bin = 1)

fig, ax = pyplot.subplots(figsize = (20,20))
ax.scatter(mass, spread, s = 0.1, edgecolor = None, alpha = 0.5)
ax.plot(centers, med, linestyle = '--', linewidth = 6, color = 'black', label = 'Median spread')
ax.plot(rad_centers, rad_med, linestyle = '--', linewidth = 6, color = 'red', label = 'Median halo diameter')
ax.legend(loc = 'lower right')
ax.loglog()
ax.set_ylabel('Spread metric [Mpc]')
ax.set_xlabel(r'Average halo mass [$M_{\odot}$]')
fig.savefig('/cosma5/data/durham/dc-murr1/spread_mass_metric_scatter.png')