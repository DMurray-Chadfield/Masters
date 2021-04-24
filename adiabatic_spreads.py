from transfer.spreadmetric import SpreadMetricCalculator
from transfer.frontends.swiftvr import SWIFTSnapshotData
from transfer.holder import SimulationData
import numpy

initial_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/eagle_0000.hdf5', halo_filename = None)
final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/eagle_0007.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties')
final_snap.stars = None

data = SimulationData(initial_snap, final_snap)

cal = SpreadMetricCalculator(simulation = data)

cal.find_neighbour_distances()
dm_spread = cal.dark_matter_spread
gas_spread = cal.gas_spread

numpy.savetxt('/cosma5/data/durham/dc-murr1/adiabatic_dm_spread.txt', dm_spread)
numpy.savetxt('/cosma5/data/durham/dc-murr1/adiabatic_gas_spread.txt', gas_spread)
