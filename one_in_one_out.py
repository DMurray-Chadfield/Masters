from transfer.spreadmetric import SpreadMetricCalculator
from transfer.frontends.swiftvr import SWIFTSnapshotData
from transfer.holder import SimulationData
import numpy
from numba import njit

initial_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0000.hdf5', halo_filename = None)
final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

haloes = final_snap.dark_matter.haloes
ids = final_snap.dark_matter.particle_ids

data = SimulationData(initial_snap, final_snap)

cal = SpreadMetricCalculator(simulation = data)

cal.find_neighbours()
neighbours = cal.dark_matter_neighbours

@njit
def one_in_one_out(halo_ids, particle_ids, neighbour_hash):

    homo = dict()
    hetero = dict()

    for i in range(len(particle_ids)):
        halo = halo_ids[i]
        neighbour = neighbour_hash[particle_ids[i]]
        neighbour_halo = halo_ids[numpy.where(particle_ids == neighbour)]
        if neighbour_halo == halo:
            homo[i] = neighbour
        else:
            hetero[i] = neighbour
        print(i)
    return len(homo), len(hetero)

homo, hetero = one_in_one_out(halo_ids = haloes, particle_ids = ids, neighbour_hash = neighbours)

print('There are %i homo pairs and %i hetero pairs' %(homo, hetero))


