import numpy
import unyt
import hist

spread = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adiabatic_gas_spread.txt'), units = 'Mpc')
mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halo_mass.txt'), units = 'msun')
neighbour_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_neighbour_halos.txt')

where = numpy.where(neighbour_halos >= 0)[0]
spread = spread[where]
mass = mass[where]

hist.plot_hist(mass,
    spread,
    r'Mass of nearest halo [$M_{\odot}$]',
    'Spread Metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_mass.png'
)


