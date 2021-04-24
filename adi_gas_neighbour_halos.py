from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy
from adi_dm_halo_dict import output
from velociraptor import load


neighbour_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_neighbour_ids.txt')
cat = load('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties')
masses = cat.masses.mass_200crit
masses.convert_to_units('msun')

neighbour_halos = numpy.zeros(len(neighbour_ids))
for i in range(len(neighbour_ids)):
    if output[int(neighbour_ids[i])] == -1:
        neighbour_halos[i] = output[int(neighbour_ids[i])]
    elif masses[output[int(neighbour_ids[i])]] < 0:
        neighbour_halos[i] = -1
    print(output[int(neighbour_ids[i])])


numpy.savetxt('/cosma5/data/durham/dc-murr1/adi_gas_neighbour_halos.txt', neighbour_halos)
