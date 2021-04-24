from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy
from dm_halo_dict import output


neighbour_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_ids.txt')



neighbour_halos = numpy.zeros(len(neighbour_ids))
for i in range(len(neighbour_ids)):
    neighbour_halos[i] = output[neighbour_ids[i]]
   

numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_neighbour_halos.txt', neighbour_halos)
