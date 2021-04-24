from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy

final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

coords = final_snap.gas.coordinates
numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_coords.txt', coords)