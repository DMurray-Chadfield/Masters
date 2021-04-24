from transfer.spreadmetric import SpreadMetricCalculator
from transfer.frontends.simbaahf import SIMBASnapshotData
from transfer.holder import SimulationData
from transfer.utils.numba import create_numba_hashtable
import numpy


initial_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_000.hdf5', halo_filename = None)

truncate_ids = {
 0: initial_snap.gas.particle_ids.max() + 1,
 1: None,
 4: initial_snap.gas.particle_ids.max() + 1,
}

final_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_151.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos', truncate_ids = truncate_ids)

data = SimulationData(initial_snap, final_snap)
cal = SpreadMetricCalculator(simulation = data)
cal.find_neighbours()


dark_matter_ids = cal.dark_matter_final_ids.value
dark_matter_coordinates = cal.dark_matter_final_coordinates.value
particle_ids = cal.gas_final_ids.value
particle_coordinates = cal.gas_final_coordinates.value
neighbours = cal.gas_neighbours

dark_matter_hashtable = create_numba_hashtable(dark_matter_ids, numpy.arange(dark_matter_ids.size))

x_dm = numpy.zeros((len(particle_ids), 3))
neighbour_ids = numpy.zeros(len(particle_ids))
for particle in range(particle_ids.size):
    id = particle_ids[particle]
    x = particle_coordinates[particle]

    nearest_dm_id = neighbours[id]
    neighbour_ids[particle] = nearest_dm_id
    nearest_dm_position = dark_matter_hashtable[nearest_dm_id]
    x_dm[particle] = dark_matter_coordinates[nearest_dm_position]

numpy.savetxt('/cosma5/data/durham/dc-murr1/simba_gas_neighbour_coords.txt', x_dm)
numpy.savetxt('/cosma5/data/durham/dc-murr1/simba_gas_neighbour_ids.txt', neighbour_ids)