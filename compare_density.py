import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy
from matplotlib.colors import LogNorm
from velociraptor.tools.lines import binned_median_line as bml
import unyt
pyplot.rcParams.update({'font.size':40})
import adi_gas_spread_density
import adi_gas_coordinate_density
import gas_spread_density
import gas_coordinate_density
import simba_gas_spread_density
import simba_gas_coordinate_density

adi_spread = adi_gas_spread_density.spread
adi_dens = adi_gas_spread_density.density
adi_xbins = numpy.logspace(numpy.log10(numpy.amin(adi_dens)), numpy.log10(numpy.amax(adi_dens)), num = 50)
adi_ybins = numpy.logspace(numpy.log10(numpy.amin(adi_spread)), numpy.log10(numpy.amax(adi_spread)), num = 50)
adi_bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.amin(adi_dens)), numpy.log10(numpy.amax(adi_dens)), num = 20), units = adi_dens.units)
adi_x = adi_gas_coordinate_density.x
adi_y = adi_gas_coordinate_density.y
adic_xbins = numpy.linspace(numpy.amin(adi_x), numpy.amax(adi_x), num = 26)
adic_ybins = numpy.linspace(numpy.amin(adi_y), numpy.amax(adi_y), num = 26)
adi_centers, adi_med, adi_err = bml(adi_dens, adi_spread, x_bins = adi_bins)


eagle_spread = gas_spread_density.spread
eagle_dens = gas_spread_density.density
eagle_xbins = numpy.logspace(numpy.log10(numpy.amin(eagle_dens)), numpy.log10(numpy.amax(eagle_dens)), num = 50)
eagle_ybins = numpy.logspace(numpy.log10(numpy.amin(eagle_spread)), numpy.log10(numpy.amax(eagle_spread)), num = 50)
eagle_bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.amin(eagle_dens)), numpy.log10(numpy.amax(eagle_dens)), num = 20), units = eagle_dens.units)
eagle_x = gas_coordinate_density.x
eagle_y = gas_coordinate_density.y
eaglec_xbins = numpy.linspace(numpy.amin(eagle_x), numpy.amax(eagle_x), num = 26)
eaglec_ybins = numpy.linspace(numpy.amin(eagle_y), numpy.amax(eagle_y), num = 26)
eagle_centers, eagle_med, eagle_err = bml(eagle_dens, eagle_spread, x_bins = eagle_bins)

simba_spread = simba_gas_spread_density.spread
simba_dens = simba_gas_spread_density.density
simba_xbins = numpy.logspace(numpy.log10(numpy.amin(simba_dens)), numpy.log10(numpy.amax(simba_dens)), num = 50)
simba_ybins = numpy.logspace(numpy.log10(numpy.amin(simba_spread)), numpy.log10(numpy.amax(simba_spread)), num = 50)
simba_bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.amin(simba_dens)), numpy.log10(numpy.amax(simba_dens)), num = 20), units = simba_dens.units)
simba_x = simba_gas_coordinate_density.x
simba_y = simba_gas_coordinate_density.y
simbac_xbins = numpy.linspace(numpy.amin(simba_x), numpy.amax(simba_x), num = 74)
simbac_ybins = numpy.linspace(numpy.amin(simba_y), numpy.amax(simba_y), num = 74)
simba_centers, simba_med, simba_err = bml(simba_dens, simba_spread, x_bins = simba_bins)


fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = pyplot.subplots(3, 2, figsize = (40, 60))

ax1.tick_params(which = 'both', direction = 'in')
ax1.tick_params(length = 10, width = 2)
ax2.tick_params(which = 'both', direction = 'in')
ax2.tick_params(length = 10, width = 2)
ax3.tick_params(which = 'both', direction = 'in')
ax3.tick_params(length = 10, width = 2)
ax4.tick_params(which = 'both', direction = 'in')
ax4.tick_params(length = 10, width = 2)
ax5.tick_params(which = 'both', direction = 'in')
ax5.tick_params(length = 10, width = 2)
ax6.tick_params(which = 'both', direction = 'in')
ax6.tick_params(length = 10, width = 2)

ax1.plot(adi_centers, adi_med, color = 'red', linewidth = 7, linestyle = '--', label = 'Adiabatic gas spread')
ax3.plot(eagle_centers, eagle_med, color = 'red', linewidth = 7, linestyle = '-', label = 'EAGLE gas spread')
ax5.plot(simba_centers, simba_med, color = 'red', linewidth = 7, linestyle = 'dashdot', label = 'SIMBA gas spread')

h1 = ax1.hist2d(adi_dens, adi_spread, bins = [adi_xbins, adi_ybins], norm = LogNorm())
h2 = ax2.hist2d(adi_x, adi_y, bins = [adic_xbins, adic_ybins], norm = LogNorm())
h3 = ax3.hist2d(eagle_dens, eagle_spread, bins = [eagle_xbins, eagle_ybins], norm = LogNorm())
h4 = ax4.hist2d(eagle_x, eagle_y, bins = [eaglec_xbins, eaglec_ybins], norm = LogNorm())
h5 = ax5.hist2d(simba_dens, simba_spread, bins = [simba_xbins, simba_ybins], norm = LogNorm())
h6 = ax6.hist2d(simba_x, simba_y, bins = [simbac_xbins, simbac_ybins], norm = LogNorm())

pyplot.colorbar(h1[3], ax=ax1)
pyplot.colorbar(h2[3], ax=ax2)
pyplot.colorbar(h3[3], ax=ax3)
pyplot.colorbar(h4[3], ax=ax4)
pyplot.colorbar(h5[3], ax=ax5)
pyplot.colorbar(h6[3], ax=ax6)

ax1.legend()
ax3.legend()
ax5.legend()

ax1.loglog()

ax3.loglog()

ax5.loglog()


ax5.set_xlabel(r'Local gas particle number density [Mpc$^{-3}$]')
ax6.set_xlabel('x coordinate [Mpc]')
ax3.set_ylabel('Spread metric [Mpc]')
ax4.set_ylabel('y coordinate [Mpc]')

fig.savefig('/cosma5/data/durham/dc-murr1/compare_density.png')



