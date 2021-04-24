from transfer.frontends.simbaahf import SIMBASnapshotData
import numpy
from scipy.spatial import cKDTree
from swiftsimio import load
import unyt
from velociraptor import load as veload
from numba import njit


initial_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_000.hdf5', halo_filename = None)

truncate_ids = {
 0: initial_snap.gas.particle_ids.max() + 1,
 1: None,
 4: initial_snap.gas.particle_ids.max() + 1,
}

final_snap = SIMBASnapshotData(
    '/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_151.hdf5',
    '/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos',
    truncate_ids = truncate_ids
)

gas_coords = final_snap.gas.coordinates
gas_coords.convert_to_units('Mpc')

boxsize = final_snap.boxsize

boxsize.to(gas_coords.units)



ball_radius = 0.5

tree = cKDTree(gas_coords, boxsize = boxsize.value)
print('searching')
nearby_particles = tree.query_ball_point(gas_coords, ball_radius, n_jobs = -1, return_length = True)
print('searched')
print(nearby_particles.shape)


numpy.savetxt('/cosma5/data/durham/dc-murr1/simba_gas_local_density.txt', nearby_particles)