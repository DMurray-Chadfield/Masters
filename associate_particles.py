from transfer.frontends.swiftvr import SWIFTSnapshotData
from velociraptor import load
import numpy

data = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

x = final_snap.dark_matter.haloes
numpy.savetxt('/cosma5/data/durham/dc-murr1/ids.txt', x)
dm_spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_spread.txt')
bound_dm_spread = dm_spread[numpy.where(x >= 0)]
x = x[numpy.where(x >= 0)]
numpy.savetxt('/cosma5/data/durham/dc-murr1/bound_dm_spread.txt', bound_dm_spread)


halo_mass = data.masses.mvir[x]
halo_radius = data.radii.rvir[x]
numpy.savetxt('/cosma5/data/durham/dc-murr1/halo_masses.txt', halo_mass)
numpy.savetxt('/cosma5/data/durham/dc-murr1/halo_radii.txt', halo_radius)

