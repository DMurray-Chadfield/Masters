import numpy 
import unyt
import hist
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib.colors import LogNorm
pyplot.rcParams.update({'font.size':40})

spread = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt'), units = 'Mpc')
distance = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_distance.txt'), units = 'Mpc')
radius = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_radius.txt'), units = 'Mpc')
mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_mass.txt'), units = 'msun')
density = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_local_density.txt'), units = 'dimensionless')
dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_halos.txt')
dm_halos = dm_halos.astype(int)


mask = numpy.where(mass > 0)[0]
spread = spread[mask]
mass = mass[mask]
dm_halos = dm_halos[mask]
radius = radius[mask]
density = density[mask]

where = numpy.where(dm_halos >= 0)[0]
spread = spread[where]
mass = mass[where]
radius = radius[where]
density = density[where]

hist.plot_hist(
    density,
    spread,
    'Number of gas particles within 500kpc radius',
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_density.png'
)

mass_cutoff = numpy.where(numpy.logical_and(mass > 10**8, mass < 10**10))[0]
spread_after = spread[mass_cutoff]
density_after = density[mass_cutoff]

spread_cutoff = numpy.where(numpy.logical_and(spread_after > 10**(-1), spread_after < 1))[0]
density_after = density_after[spread_cutoff]
spread_after = spread_after[spread_cutoff]

xbins = numpy.logspace(numpy.log10(numpy.amin(density)), numpy.log10(numpy.amax(density)), num = 50)
ybins = numpy.logspace(numpy.log10(numpy.amin(spread)), numpy.log10(numpy.amax(spread)), num = 50)


fig, (ax1, ax2) = pyplot.subplots(1,2, figsize = (40, 20), sharey = True, sharex = True)

ax1.tick_params(which = 'both', direction = 'in')
ax1.tick_params(length = 10, width = 2)
ax2.tick_params(which = 'both', direction = 'in')
ax2.tick_params(length = 10, width = 2)

h1 = ax1.hist2d(density, spread, bins = [xbins, ybins], norm = LogNorm())
h2 = ax2.hist2d(density_after, spread_after, bins = [xbins, ybins], norm = LogNorm())

pyplot.colorbar(h1[3], ax=ax1)
pyplot.colorbar(h2[3], ax=ax2)

ax1.loglog()
ax2.loglog()

fig.savefig('/cosma5/data/durham/dc-murr1/gas_compare_density.png')