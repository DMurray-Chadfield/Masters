from transfer.frontends.swiftvr import SWIFTSnapshotData
from scipy.spatial import cKDTree
import numpy


final = SWIFTSnapshotData(
    '/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5',
    '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties',
)

boxsize = final.boxsize
boxsize.convert_to_units('Mpc')
dm_coords = final.dark_matter.coordinates
halo_coords = final.halo_coordinates
dm_coords.convert_to_units('Mpc')
halo_coords.convert_to_units('Mpc')

tree = cKDTree(halo_coords, boxsize = boxsize.value)
d, i = tree.query(dm_coords, k = 1, n_jobs = -1)

numpy.savetxt('/cosma5/data/durham/dc-murr1/dm_nearest_halo_distance.txt', d)
numpy.savetxt('/cosma5/data/durham/dc-murr1/dm_nearest_halos.txt', i)