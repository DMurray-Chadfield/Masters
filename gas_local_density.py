from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy
from scipy.spatial import cKDTree
from swiftsimio import load
import unyt
from velociraptor import load as veload
from numba import njit


final_snap = SWIFTSnapshotData(
    filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5',
    halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties'
)

gas_coords = final_snap.gas.coordinates
boxsize = final_snap.boxsize
boxsize.to(gas_coords.units)


ball_radius = 0.5

tree = cKDTree(gas_coords, boxsize = boxsize.value)
print('searching')
nearby_particles = tree.query_ball_point(gas_coords, ball_radius, n_jobs = -1, return_length = True)
print('searched')
print(nearby_particles.shape)


numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_local_density.txt', nearby_particles)