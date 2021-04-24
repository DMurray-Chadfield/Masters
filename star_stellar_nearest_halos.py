from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy
from scipy.spatial import cKDTree
from velociraptor import load


final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
star_coords = numpy.loadtxt('/cosma5/data/durham/dc-murr1/star_coords.txt')
cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
halo_coords = numpy.loadtxt('/cosma5/data/durham/dc-murr1/halos.txt', usecols = (0,1,2))
masses = cat.masses.mass_200crit_star
struc = cat.structure_type.structuretype 
halo_coords = halo_coords[numpy.where(struc == 10)[0], :]
masses = masses[numpy.where(struc == 10)[0]]
halo_coords = halo_coords[numpy.where(masses > 0)[0], :]

boxsize = final_snap.boxsize
boxsize.to(final_snap.dark_matter.coordinates.units)

tree = cKDTree(halo_coords, boxsize = boxsize.value)
d, i = tree.query(star_coords, k = 10, n_jobs = -1)

numpy.savetxt('/cosma5/data/durham/dc-murr1/star_stellar_nearest_halos.txt', i)