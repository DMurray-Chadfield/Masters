import numpy 
import unyt
import hist
import dm_compare_mass
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
from matplotlib.colors import LogNorm
from velociraptor.tools.lines import binned_median_line as bml

spread = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adiabatic_gas_spread.txt'), units = 'Mpc')
distance = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halo_distance.txt'), units = 'Mpc')
radius = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halo_radius.txt'), units = 'Mpc')
mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halo_mass.txt'), units = 'msun')
dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_neighbour_halos.txt')
dm_halos = dm_halos.astype(int)


frac_distance = distance / radius

mask = numpy.where(mass > 0)[0]
spread = spread[mask]
frac_distance = frac_distance[mask]
mass = mass[mask]
dm_halos = dm_halos[mask]
radius = radius[mask]


hist.plot_hist(
    mass,
    spread,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/adi_gas_spread_mass.png'
)

where = numpy.where(dm_halos >= 0)[0]
spread = spread[where]
frac_distance = frac_distance[where]
mass = mass[where]
radius = radius[where]

hist.plot_hist(
    mass,
    spread,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_mass.png'
)

xbins = numpy.logspace(numpy.log10(numpy.amin(mass)), numpy.log10(numpy.amax(mass)), num = 50)
ybins = numpy.logspace(numpy.log10(numpy.amin(spread)), numpy.log10(numpy.amax(spread)), num = 50)
bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.amin(mass)), numpy.log10(numpy.amax(mass)), num = 20), units = mass.units)
centers, med, err = bml(mass, spread, x_bins = bins)
halo_centers, halo_med, halo_err = bml(mass, radius, x_bins = bins)

simba_centers, simba_med = dm_compare_mass.simba_centers, dm_compare_mass.simba_med
eagle_centers, eagle_med = dm_compare_mass.eagle_centers, dm_compare_mass.eagle_med


fig, (ax1, ax2) = pyplot.subplots(1, 2, figsize = (40,20), sharey = True)
ax1.tick_params(which = 'both', direction = 'in')
ax1.tick_params(length = 10, width = 2)
ax2.tick_params(which = 'both', direction = 'in')
ax2.tick_params(length = 10, width = 2)
h = ax1.hist2d(mass, spread, bins = [xbins, ybins], norm = LogNorm())
pyplot.colorbar(h[3], ax=ax1)
ax1.plot(centers, med, linestyle = '--', linewidth = 7, color = 'red', label = 'Adiabatic spread')
ax1.plot(halo_centers, halo_med, linestyle = '--', linewidth = 7, color = 'fuchsia', label = 'Adiabatic radius')

ax2.plot(centers, med, linestyle = '--', linewidth = 7, color = 'orange', label = 'Adiabatic spread')
ax2.plot(simba_centers, simba_med, linestyle = 'dashdot', linewidth = 7, color = 'blue', label = 'SIMBA DM spread')
ax2.plot(eagle_centers, eagle_med, linestyle = '-', linewidth = 7, color = 'blue', label = 'EAGLE DM spread')
ax2.plot(halo_centers, halo_med, linestyle = '--', linewidth = 7, color = 'fuchsia', label = 'Adiabatic radius')

ax1.loglog()
ax2.loglog()
ax1.legend()
ax2.legend()

fig.add_subplot(111, frame_on=False)
pyplot.tick_params(labelcolor="none", bottom=False, left=False)

pyplot.ylabel("Spread metric [Mpc]", labelpad = 25)
pyplot.xlabel(r"Nearest halo mass [M$_\odot$]")

fig.savefig('/cosma5/data/durham/dc-murr1/adi_compare_mass.png')


'''
one = numpy.where(numpy.logical_and(numpy.amin(frac_distance) < frac_distance, frac_distance < numpy.percentile(frac_distance, 25)))[0]
two = numpy.where(numpy.logical_and(numpy.percentile(frac_distance, 25) < frac_distance, frac_distance < numpy.percentile(frac_distance, 50)))[0]
three = numpy.where(numpy.logical_and(numpy.percentile(frac_distance, 50) < frac_distance, frac_distance < numpy.percentile(frac_distance, 75)))[0]
four = numpy.where(numpy.logical_and(numpy.percentile(frac_distance, 75) < frac_distance, frac_distance < numpy.amax(frac_distance)))[0]

spread_one = frac_spread[one]
mass_one = mass[one]
spread_two = frac_spread[two]
mass_two = mass[two]
spread_three = frac_spread[three]
mass_three = mass[three]
spread_four = frac_spread[four]
mass_four = mass[four]

hist.plot_hist(
    mass_one,
    spread_one,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_mass_0_25.png'
)

hist.plot_hist(
    mass_two,
    spread_two,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_mass_25_50.png'
)

hist.plot_hist(
    mass_three,
    spread_three,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_mass_50_75.png'
)

hist.plot_hist(
    mass_four,
    spread_four,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_mass_75_100.png'
)
'''