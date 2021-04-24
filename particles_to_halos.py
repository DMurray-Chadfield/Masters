from transfer.spreadmetric import SpreadMetricCalculator
from transfer.holder import SimulationData
from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy

initial_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0000.hdf5',
                                 halo_filename = None)
final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5',
                               halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

simdata = SimulationData(initial_snap, final_snap)

cal = SpreadMetricCalculator(simulation = simdata)
cal.find_neighbour_distances()

halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/ids.txt')
dm_ids = cal.dark_matter_initial_ids.value[numpy.where(halos >= 0)]
halos = halos[numpy.where(halos >= 0)]

dm_halos = dict()
for i in range(len(dm_ids)):
    dm_halos[dm_ids[i]] = halos[i]

numpy.save('/cosma5/data/durham/dc-murr1/dm_halos.txt', dm_halos)