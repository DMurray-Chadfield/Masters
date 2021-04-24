import numpy 
import unyt
import hist

spread = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_spread.txt'), units = 'Mpc')
distance = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_nearest_halo_distance.txt'), units = 'Mpc')
radius = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_nearest_halo_radius.txt'), units = 'Mpc')
mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_nearest_halo_mass.txt'), units = 'msun')
dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_neighbour_halos.txt')
dm_halos = dm_halos.astype(int)

spread = spread
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
    '/cosma5/data/durham/dc-murr1/dm_spread_mass.png'
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
    '/cosma5/data/durham/dc-murr1/dm_neighbour_spread_mass.png'
)

one = numpy.where(numpy.logical_and(numpy.amin(frac_distance) < frac_distance, frac_distance < numpy.percentile(frac_distance, 25)))[0]
two = numpy.where(numpy.logical_and(numpy.percentile(frac_distance, 25) < frac_distance, frac_distance < numpy.percentile(frac_distance, 50)))[0]
three = numpy.where(numpy.logical_and(numpy.percentile(frac_distance, 50) < frac_distance, frac_distance < numpy.percentile(frac_distance, 75)))[0]
four = numpy.where(numpy.logical_and(numpy.percentile(frac_distance, 75) < frac_distance, frac_distance < numpy.amax(frac_distance)))[0]

spread_one = spread[one]
mass_one = mass[one]
spread_two = spread[two]
mass_two = mass[two]
spread_three = spread[three]
mass_three = mass[three]
spread_four = spread[four]
mass_four = mass[four]

hist.plot_hist(
    mass_one,
    spread_one,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/dm_neighbour_spread_mass_0_25.png'
)

hist.plot_hist(
    mass_two,
    spread_two,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/dm_neighbour_spread_mass_25_50.png'
)

hist.plot_hist(
    mass_three,
    spread_three,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/dm_neighbour_spread_mass_50_75.png'
)

hist.plot_hist(
    mass_four,
    spread_four,
    r'Nearest halo mass [$M_{\odot}$]',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/dm_neighbour_spread_mass_75_100.png'
)