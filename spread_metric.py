from transfer.spreadmetric import SpreadMetricCalculator
from transfer.frontends.swiftvr import SWIFTSnapshotData
from transfer.holder import SimulationData
import numpy

initial_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0000.hdf5', halo_filename = None)
final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

data = SimulationData(initial_snap, final_snap)

cal = SpreadMetricCalculator(simulation = data)

cal.find_neighbour_distances()
dm_spread = cal.dark_matter_spread
gas_spread = cal.gas_spread
star_spread = cal.star_spread
numpy.savetxt('/cosma5/data/durham/dc-murr1/dm_spread.txt', dm_spread)
numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_spread.txt', gas_spread)
numpy.savetxt('/cosma5/data/durham/dc-murr1/star_spread.txt', star_spread)



