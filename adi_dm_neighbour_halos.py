import numpy
from adi_dm_halo_dict import output
from velociraptor import load


neighbour_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_dm_neighbour_ids.txt')

neighbour_halos = numpy.zeros(len(neighbour_ids))
for i in range(len(neighbour_ids)):
    neighbour_halos[i] = output[int(neighbour_ids[i])]
   

numpy.savetxt('/cosma5/data/durham/dc-murr1/adi_dm_neighbour_halos.txt', neighbour_halos)