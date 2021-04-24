import numpy 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
from matplotlib.colors import LogNorm
from velociraptor import load
import unyt
from velociraptor.tools.lines import binned_median_line as bml
import hist


cat = load('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties')
distance = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halo_distance.txt'), units = 'Mpc')
spread = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adiabatic_gas_spread.txt'), units = 'Mpc')
radius = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halo_radius.txt'), units = 'Mpc')
#frac_spread = spread / radius
#frac_distance = distance / radius
dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_neighbour_halos.txt').astype(int)
mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halo_mass.txt'), units = 'msun')

where = numpy.where(dm_halos >= 0)[0]
spread = spread[where]
distance = distance[where]
mass = mass[where]

hist.plot_hist(distance,
            spread,
            'Distance to nearest halo [Mpc]',
            'Spread metric [Mpc]',
            '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_distance.png')

one = numpy.where(numpy.logical_and(numpy.amin(mass) < mass, mass < numpy.percentile(mass, 25)))[0]
two = numpy.where(numpy.logical_and(numpy.percentile(mass, 25) < mass, mass < numpy.percentile(mass, 50)))[0]
three = numpy.where(numpy.logical_and(numpy.percentile(mass, 50) < mass, mass < numpy.percentile(mass, 75)))[0]
four = numpy.where(numpy.logical_and(numpy.percentile(mass, 75) < mass, mass < numpy.amax(mass)))[0]

spread_one = spread[one]
distance_one = distance[one]
spread_two = spread[two]
distance_two = distance[two]
spread_three = spread[three]
distance_three = distance[three]
spread_four = spread[four]
distance_four = distance[four]


hist.plot_hist(
    distance_one,
    spread_one,
    'Distance to nearest halo [Mpc]',
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_distance_0_25.png'
)

hist.plot_hist(
    distance_two,
    spread_two,
    'Distance to nearest halo [Mpc]',
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_distance_25_50.png'
)

hist.plot_hist(
    distance_three,
    spread_three,
    'Distance to nearest halo [Mpc]',
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_distance_50_75.png'
)

hist.plot_hist(
    distance_four,
    spread_four,
    'Distance to nearest halo [Mpc]',
    'Spread metric [Mpc]',
    '/cosma5/data/durham/dc-murr1/adi_gas_neighbour_spread_distance_75_100.png'
)