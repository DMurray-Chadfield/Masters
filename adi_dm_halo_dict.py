from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy

final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/eagle_0007.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties')

dm_halos = final_snap.dark_matter.haloes
dm_ids = final_snap.dark_matter.particle_ids.value

output = dict()

for i in range(len(dm_ids)):
    output[dm_ids[i]] = dm_halos[i]