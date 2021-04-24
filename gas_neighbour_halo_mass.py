from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy
from scipy.spatial import cKDTree
from velociraptor import load


final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
neighbour_coords = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_coords.txt')
cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
halo_coords = numpy.loadtxt('/cosma5/data/durham/dc-murr1/halos.txt', usecols = (0,1,2))
masses = cat.masses.mass_200crit
struc = cat.structure_type.structuretype 
halo_coords = halo_coords[numpy.where(struc == 10)[0], :]
masses = masses[numpy.where(struc == 10)[0]]
halo_coords = halo_coords[numpy.where(masses > 0)[0]]
masses = masses[numpy.where(masses > 0)[0]]
masses.convert_to_units('msun')

boxsize = final_snap.boxsize
boxsize.to(final_snap.gas.coordinates.units)

tree = cKDTree(halo_coords, boxsize = boxsize.value)
d, halos = tree.query(neighbour_coords, k = 1, n_jobs = -1)

halos = halos.astype(int)
halo_masses = masses[halos]

numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_neighbour_halo_mass.txt', halo_masses)