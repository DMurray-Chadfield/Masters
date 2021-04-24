from velociraptor import load
import numpy

cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
bh_mass = cat.black_hole_masses.max
bh_mass.convert_to_units('msun')

halo_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halos.txt')
halo_ids = halo_ids.astype(int)

nearest_bh_mass = bh_mass[halo_ids]

numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_nearest_bh_mass.txt', nearest_bh_mass)

