import numpy
from velociraptor import load
from numba import njit

halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_stellar_nearest_halos.txt')
halos = halos.astype(int)
cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
radii = cat.radii.r_200crit
struc = cat.structure_type.structuretype
radii = radii[numpy.where(struc == 10)[0]]
radii = radii[numpy.where(radii > 0)[0]]
radii.convert_to_units('Mpc')


@njit
def find_average_radius(x, r):
    average = numpy.zeros(len(x[:,0]))
    for i in range(len(average)):
        halo_radii = r[halos[i,:]]
        average[i] = numpy.mean(halo_radii)
        if i in range(0, 6400000, 100000):
            print(i)
    return average


average_halo_mass = find_average_radius(halos, radii)
numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_average_stellar_radius.txt', average_halo_mass)