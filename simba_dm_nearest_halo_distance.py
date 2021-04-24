from transfer.frontends.simbaahf import SIMBASnapshotData
from scipy.spatial import cKDTree
import numpy

initial_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_000.hdf5', halo_filename = None)

truncate_ids = {
 0: initial_snap.gas.particle_ids.max() + 1,
 1: None,
 4: initial_snap.gas.particle_ids.max() + 1,
}

final = SIMBASnapshotData(
    '/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_151.hdf5',
    '/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos',
    truncate_ids = truncate_ids
)

boxsize = final.boxsize
boxsize.convert_to_units('Mpc')
dm_coords = final.dark_matter.coordinates
halo_coords = final.halo_coordinates
dm_coords.convert_to_units('Mpc')
halo_coords.convert_to_units('Mpc')

tree = cKDTree(halo_coords, boxsize = boxsize.value)
d, i = tree.query(dm_coords, k = 1, n_jobs = -1)

numpy.savetxt('/cosma5/data/durham/dc-murr1/simba_dm_nearest_halo_distance.txt', d)
numpy.savetxt('/cosma5/data/durham/dc-murr1/simba_dm_nearest_halos.txt', i)