import numpy
import unyt
import hist

spread = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt'), units = 'Mpc')
bh_mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_bh_mass.txt'), units = 'msun')
mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_mass.txt'), units = 'msun')
where_bh = numpy.where(bh_mass > 0)[0]
spread = spread[where_bh]
bh_mass = bh_mass[where_bh]
mass = mass[where_bh]

hist.plot_hist(
    bh_mass,
    spread,
    r"Mass of nearest halo's central BH [$M_{\odot}$]",
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/gas_spread_bh.png'
)

dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_halos.txt')
dm_halos = dm_halos.astype(int)
dm_halos = dm_halos[where_bh]

where = numpy.where(dm_halos >= 0)[0]

spread = spread[where]
bh_mass = bh_mass[where]
mass = mass[where]

hist.plot_hist(
    bh_mass,
    spread,
    r"Mass of nearest halo's central BH [$M_{\odot}$]",
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_bh.png'
)

one = numpy.where(numpy.logical_and(numpy.amin(mass) < mass, mass < numpy.percentile(mass, 25)))[0]
two = numpy.where(numpy.logical_and(numpy.percentile(mass, 25) < mass, mass < numpy.percentile(mass, 50)))[0]
three = numpy.where(numpy.logical_and(numpy.percentile(mass, 50) < mass, mass < numpy.percentile(mass, 75)))[0]
four = numpy.where(numpy.logical_and(numpy.percentile(mass, 75) < mass, mass < numpy.amax(mass)))[0]

spread_one = spread[one]
bh_one = bh_mass[one]
spread_two = spread[two]
bh_two = bh_mass[two]
spread_three = spread[three]
bh_three = bh_mass[three]
spread_four = spread[four]
bh_four = bh_mass[four]

hist.plot_hist(
    bh_one,
    spread_one,
    r"Mass of nearest halo's central BH [$M_{\odot}$]",
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_bh_0_25.png'
)

hist.plot_hist(
    bh_two,
    spread_two,
    r"Mass of nearest halo's central BH [$M_{\odot}$]",
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_bh_25_50.png'
)

hist.plot_hist(
    bh_three,
    spread_three,
    r"Mass of nearest halo's central BH [$M_{\odot}$]",
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_bh_50_75.png'
)

hist.plot_hist(
    bh_four,
    spread_four,
    r"Mass of nearest halo's central BH [$M_{\odot}$]",
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/gas_neighbour_spread_bh_75_100.png'
)
