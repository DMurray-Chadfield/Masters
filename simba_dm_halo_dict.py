from transfer.frontends.simbaahf import SIMBASnapshotData
import numpy

initial_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_000.hdf5', halo_filename = None)

truncate_ids = {
 0: initial_snap.gas.particle_ids.max() + 1,
 1: None,
 4: initial_snap.gas.particle_ids.max() + 1,
}

final_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_151.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos', truncate_ids = truncate_ids)

dm_halos = final_snap.dark_matter.haloes
dm_ids = final_snap.dark_matter.particle_ids.value

output = dict()

for i in range(len(dm_ids)):
    output[dm_ids[i]] = dm_halos[i]
