from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy
from numba import njit

data = SWIFTSnapshotData(filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5',
                         halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
halo_coords = data.halo_coordinates.value
dm_coords = data.dark_matter.coordinates.value
halo_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/ids.txt')

@njit
def find_displacements(halo_coords, dm_coords, halo_ids):
    
    dm_coords = dm_coords[numpy.where(halo_ids >= 0)]
    halo_ids = halo_ids[numpy.where(halo_ids >= 0)]
    halo_ids = halo_ids.astype(numpy.int64)
    halo_coords = halo_coords[halo_ids, :]

    displacements = numpy.zeros(len(dm_coords[:,0]))
    for i in range(len(dm_coords[:,0])):
        x_diff = dm_coords[i,0] - halo_coords[i,0]
        y_diff = dm_coords[i,1] - halo_coords[i,1]
        z_diff = dm_coords[i,2] - halo_coords[i,2]
        vec = numpy.sqrt(x_diff**2 + y_diff**2 + z_diff**2)
        if vec > 1:
            vec = numpy.absolute(25 - vec)
        displacements[i] = vec
        
    return displacements

disp = find_displacements(halo_coords, dm_coords, halo_ids)
print(disp[1308])
numpy.savetxt('/cosma5/data/durham/dc-murr1/dm_displacements.txt', disp)