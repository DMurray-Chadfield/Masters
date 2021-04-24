import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy
from matplotlib.colors import LogNorm
from velociraptor.tools.lines import binned_median_line as bml
import unyt
pyplot.rcParams.update({'font.size':40})
import dm_spread_mass
import simba_dm_spread_mass
from velociraptor import load

simba_spread = simba_dm_spread_mass.spread
simba_mass = simba_dm_spread_mass.mass
simba_xbins = numpy.logspace(numpy.log10(numpy.amin(simba_mass)), numpy.log10(numpy.amax(simba_mass)), num = 50)
simba_ybins = numpy.logspace(numpy.log10(numpy.amin(simba_spread)), numpy.log10(numpy.amax(simba_spread)), num = 50)
simba_bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.amin(simba_mass)), numpy.log10(numpy.amax(simba_mass)), num = 20), units = simba_mass.units)
simba_centers, simba_med, simba_err = bml(simba_mass, simba_spread, x_bins = simba_bins)
simba_radius = simba_dm_spread_mass.radius
simba_halo_centers, simba_halo_med, simba_halo_err = bml(simba_mass, simba_radius, x_bins = simba_bins)

eagle_spread = dm_spread_mass.spread
eagle_mass = dm_spread_mass.mass
eagle_xbins = numpy.logspace(numpy.log10(numpy.amin(eagle_mass)), numpy.log10(numpy.amax(eagle_mass)), num = 50)
eagle_ybins = numpy.logspace(numpy.log10(numpy.amin(eagle_spread)), numpy.log10(numpy.amax(eagle_spread)), num = 50)
eagle_bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.amin(eagle_mass)), numpy.log10(numpy.amax(eagle_mass)), num = 20), units = eagle_mass.units)
eagle_centers, eagle_med, eagle_err = bml(eagle_mass, eagle_spread, x_bins = eagle_bins)
eagle_radius = dm_spread_mass.radius
eagle_halo_centers, eagle_halo_med, eagle_halo_err = bml(eagle_mass, eagle_radius, x_bins = eagle_bins)
#remember to mask radius and remove frac spread

fig, (ax1, ax2, ax3) = pyplot.subplots(1,3, figsize = (60, 20), sharey = True)


ax1.tick_params(which = 'both', direction = 'in')
ax1.tick_params(length = 10, width = 2)
ax2.tick_params(which = 'both', direction = 'in')
ax2.tick_params(length = 10, width = 2)
ax3.tick_params(which = 'both', direction = 'in')
ax3.tick_params(length = 10, width = 2)

h1 = ax1.hist2d(eagle_mass, eagle_spread, bins = [eagle_xbins, eagle_ybins], norm = LogNorm())
h2 = ax2.hist2d(simba_mass, simba_spread, bins = [simba_xbins, simba_ybins], norm = LogNorm())
pyplot.colorbar(h1[3], ax=ax1)
pyplot.colorbar(h2[3], ax=ax2)

ax1.plot(eagle_centers, eagle_med, linestyle = '-', linewidth = 7, color = 'red', label = 'EAGLE spread')
ax1.plot(eagle_halo_centers, eagle_halo_med, linestyle = '-', linewidth = 7, color = 'fuchsia', label = 'EAGLE radius')
ax2.plot(simba_centers, simba_med, linestyle = 'dashdot', linewidth = 7, color = 'red', label = 'SIMBA spread')
ax2.plot(simba_halo_centers, simba_halo_med, linestyle = 'dashdot', linewidth = 7, color = 'fuchsia', label = 'SIMBA radius')


ax3.set_xlim(numpy.amin(eagle_mass), numpy.amax(simba_mass))

ax1.legend()
ax2.legend()

ax1.loglog()
ax2.loglog()
ax3.loglog()

ax3.plot(eagle_centers, eagle_med, linestyle = '-', linewidth = 7, color = 'red', label = 'EAGLE spread')
ax3.plot(simba_centers, simba_med, linestyle = 'dashdot', linewidth = 7, color = 'red', label = 'SIMBA spread')
ax3.plot(eagle_halo_centers, eagle_halo_med, linestyle = '-', linewidth = 7, color = 'fuchsia', label = 'EAGLE radius')
ax3.plot(simba_halo_centers, simba_halo_med, linestyle = 'dashdot', linewidth = 7, color = 'fuchsia', label = 'SIMBA radius')
ax3.legend()

ax1.tick_params(axis='x', which='major', pad=10)
ax2.tick_params(axis='x', which='major', pad=10)
ax3.tick_params(axis='x', which='major', pad=10)

fig.add_subplot(111, frame_on=False)
pyplot.tick_params(labelcolor="none", bottom=False, left=False)

pyplot.ylabel("Spread metric [Mpc]", labelpad = 20)
pyplot.xlabel(r"Nearest halo mass [M$_\odot$]")

fig.savefig('/cosma5/data/durham/dc-murr1/dm_compare_mass.png')
