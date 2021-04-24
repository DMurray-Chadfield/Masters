from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy

final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/eagle_0007.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties')

coords = final_snap.gas.coordinates
numpy.savetxt('/cosma5/data/durham/dc-murr1/adi_gas_coords.txt', coords)