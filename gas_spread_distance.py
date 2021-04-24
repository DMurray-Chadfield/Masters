import numpy 
import unyt
import hist

spread = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt'), units = 'Mpc')
distance = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_distance.txt'), units = 'Mpc')
radius = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_radius.txt'), units = 'Mpc')
mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_mass.txt'), units = 'msun')
dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_halos.txt')
dm_halos = dm_halos.astype(int)

frac_spread = spread / radius
frac_distance = distance / radius

mask = numpy.where(frac_distance > 10**(-4))[0]
frac_spread = frac_spread[mask]
frac_distance = frac_distance[mask]
mass = mass[mask]
dm_halos = dm_halos[mask]


hist.plot_hist(
    frac_distance,
    frac_spread,
    'Distance to nearest halo / halo radius',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/gas_spread_distance.png'
)

where = numpy.where(dm_halos >= 0)[0]
frac_spread = frac_spread[where]
frac_distance = frac_distance[where]
mass = mass[where]

hist.plot_hist(
    frac_distance,
    frac_spread,
    'Distance to nearest halo / halo radius',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_distance.png'
)

one = numpy.where(numpy.logical_and(numpy.amin(mass) < mass, mass < numpy.percentile(mass, 25)))[0]
two = numpy.where(numpy.logical_and(numpy.percentile(mass, 25) < mass, mass < numpy.percentile(mass, 50)))[0]
three = numpy.where(numpy.logical_and(numpy.percentile(mass, 50) < mass, mass < numpy.percentile(mass, 75)))[0]
four = numpy.where(numpy.logical_and(numpy.percentile(mass, 75) < mass, mass < numpy.amax(mass)))[0]

spread_one = frac_spread[one]
distance_one = frac_distance[one]
spread_two = frac_spread[two]
distance_two = frac_distance[two]
spread_three = frac_spread[three]
distance_three = frac_distance[three]
spread_four = frac_spread[four]
distance_four = frac_distance[four]

hist.plot_hist(
    distance_one,
    spread_one,
    'Distance to nearest halo / halo radius',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_distance_0_25.png'
)

hist.plot_hist(
    distance_two,
    spread_two,
    'Distance to nearest halo / halo radius',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_distance_25_50.png'
)

hist.plot_hist(
    distance_three,
    spread_three,
    'Distance to nearest halo / halo radius',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_distance_50_75.png'
)

hist.plot_hist(
    distance_four,
    spread_four,
    'Distance to nearest halo / halo radius',
    'Spread metric / halo radius',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_distance_75_100.png'
)