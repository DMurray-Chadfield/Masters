import unyt
import numpy
from velociraptor import load

cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
masses = cat.masses.mass_200crit
masses.convert_to_units('msun')

halo_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halos.txt')
halo_ids = halo_ids.astype(int)

halo_masses = masses[halo_ids]

numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_nearest_halo_mass.txt', halo_masses)