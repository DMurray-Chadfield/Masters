import numpy
from velociraptor import load

cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_halos.txt')
struc = cat.structure_type.structuretype

where = numpy.where(dm_halos >= 0)[0]
dm_halos = dm_halos[where]
dm_halos = dm_halos.astype(int)
dm_halo_structure = struc[dm_halos]
print(numpy.amin(dm_halo_structure))