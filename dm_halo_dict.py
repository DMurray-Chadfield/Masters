from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy

final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

dm_halos = final_snap.dark_matter.haloes
dm_ids = final_snap.dark_matter.particle_ids.value

output = dict()

for i in range(len(dm_ids)):
    output[dm_ids[i]] = dm_halos[i]

