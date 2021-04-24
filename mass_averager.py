import numpy
from velociraptor import load
from numba import njit

halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/nearest_halos.txt')
halos = halos.astype(int)
cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
masses = cat.masses.mass_200crit
struc = cat.structure_type.structuretype
masses = masses[numpy.where(struc == 10)[0]]
masses = masses[numpy.where(masses > 0)[0]]
masses.convert_to_units('msun')


@njit
def find_average(x, m):
    average = numpy.zeros(len(x[:,0]))
    for i in range(len(average)):
        halo_masses = m[halos[i,:]]
        average[i] = numpy.mean(halo_masses)
        if i in range(0, 6400000, 100000):
            print(i)
    return average


average_halo_mass = find_average(halos, masses)
numpy.savetxt('/cosma5/data/durham/dc-murr1/average_halo_mass.txt', average_halo_mass)

