from transfer.spreadmetric import SpreadMetricCalculator
from transfer.holder import SimulationData
from transfer.frontends.swiftvr import SWIFTSnapshotData

initial_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0000.hdf5',
                                 halo_filename = None)
final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5',
                               halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

simdata = SimulationData(initial_snap, final_snap)

cal = SpreadMetricCalculator(simulation = simdata)
cal.find_neighbour_distances()
print(len(cal.dark_matter_neighbours))
