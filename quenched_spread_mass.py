import numpy 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
from matplotlib.colors import LogNorm
from velociraptor import load
import unyt
from velociraptor.tools.lines import binned_median_line as bml

cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
sfr = cat.star_formation_rate.sfr_gas
sfr.convert_to_units(unyt.msun / unyt.yr)
masses = cat.masses.m_star_30kpc
spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt')
dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_halos.txt')

where = numpy.where(dm_halos >= 0)[0]
spread = spread[where]
dm_halos = dm_halos[where]
dm_halos = dm_halos.astype(int)

non_halos = []
for i in range(len(dm_halos)):
    if masses[dm_halos[i]] <= 0:
        non_halos.append(i)

dm_halos = numpy.delete(dm_halos, non_halos)
spread = numpy.delete(spread, non_halos)

halo_sfr = sfr[dm_halos]
masses = masses[dm_halos]

where_quenched = numpy.where(halo_sfr == 0)[0]
masses = masses[where_quenched]
spread = spread[where_quenched]

masses.convert_to_units(unyt.msun)

fig, ax = pyplot.subplots(figsize = (20,20))
x_bins = numpy.logspace(numpy.log10(numpy.amin(masses)), numpy.log10(numpy.amax(masses)), num = 100)
bins = numpy.logspace(numpy.log10(numpy.amin(masses)), numpy.log10(numpy.amax(masses)), num = 20)
y_bins = numpy.logspace(numpy.log10(numpy.amin(spread)), numpy.log10(numpy.amax(spread)), num = 100)
h = ax.hist2d(masses, spread, bins = [x_bins, y_bins], norm = LogNorm())
pyplot.colorbar(h[3], ax=ax)
ax.loglog()
ax.set_ylabel("Spread metric [Mpc]")
ax.set_xlabel(r"Stellar mass of neighbour's halo $[M_{\odot}]$")
ax.tick_params(which = 'both', direction = 'in')
ax.tick_params(length = 10, width = 3)

bins = unyt.unyt_array(bins, units = 'msun')
spread = unyt.unyt_array(spread, units = 'Mpc')

centers, med, err = bml(masses, spread, x_bins = bins)
ax.plot(centers, med, linestyle = '--', linewidth = 6, color = 'red')

fig.savefig('/cosma5/data/durham/dc-murr1/quenched_spread_mass.png')
