import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy
from matplotlib.colors import LogNorm
from velociraptor.tools.lines import binned_median_line as bml
import unyt
pyplot.rcParams.update({'font.size':40})
import dm_compare_mass
import adi_gas_spread_mass as adi_spread_mass
import gas_compare_mass


eagle_dm_centers = dm_compare_mass.eagle_centers
eagle_dm_med = dm_compare_mass.eagle_med
simba_dm_centers = dm_compare_mass.simba_centers
simba_dm_med = dm_compare_mass.simba_med
adi_centers = adi_spread_mass.centers
adi_med = adi_spread_mass.med
eagle_gas_centers = gas_compare_mass.eagle_centers
eagle_gas_med = gas_compare_mass.eagle_med
simba_gas_centers = gas_compare_mass.simba_centers
simba_gas_med = gas_compare_mass.simba_med


fig, ax = pyplot.subplots(figsize = (20, 20))

ax.tick_params(which = 'both', direction = 'in')
ax.tick_params(length = 10, width = 2)

ax.plot(eagle_dm_centers, eagle_dm_med, linestyle = '-', linewidth = 7, color = 'blue', label = 'EAGLE DM spread')
ax.plot(simba_dm_centers, simba_dm_med, linestyle = 'dashdot', linewidth = 7, color = 'blue', label = 'SIMBA DM spread')
ax.plot(adi_centers, adi_med, linestyle = '--', linewidth = 7, color = 'orange', label = 'Adiabatic gas spread')
ax.plot(eagle_gas_centers, eagle_gas_med, linestyle = '-', linewidth = 7, color = 'orange', label = 'EAGLE gas spread')
ax.plot(simba_gas_centers, simba_gas_med, linestyle = 'dashdot', linewidth = 7, color = 'orange', label = 'SIMBA gas spread')

ax.set_ylabel('Spread metric [Mpc]')
ax.set_xlabel(r'Nearest halo mass [M$_\odot$]')

ax.legend()
ax.loglog()

fig.savefig('/cosma5/data/durham/dc-murr1/compare_all_mass.png')