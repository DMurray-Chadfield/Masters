from transfer.frontends.swiftvr import SWIFTSnapshotData
from scipy.spatial import cKDTree
import numpy


final = SWIFTSnapshotData(
    '/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/eagle_0007.hdf5',
    '/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties',
)

boxsize = final.boxsize
boxsize.convert_to_units('Mpc')
dm_coords = final.dark_matter.coordinates
halo_coords = final.halo_coordinates
dm_coords.convert_to_units('Mpc')
halo_coords.convert_to_units('Mpc')

tree = cKDTree(halo_coords, boxsize = boxsize.value)
d, i = tree.query(dm_coords, k = 1, n_jobs = -1)

numpy.savetxt('/cosma5/data/durham/dc-murr1/adi_dm_nearest_halo_distance.txt', d)
numpy.savetxt('/cosma5/data/durham/dc-murr1/adi_dm_nearest_halos.txt', i)