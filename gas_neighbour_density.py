from transfer.frontends.swiftvr import SWIFTSnapshotData
import numpy
from scipy.spatial import cKDTree
from swiftsimio import load
import unyt
from velociraptor import load as veload
from numba import njit


cat = veload('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')



final_snap = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
gas_coords = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_coords.txt')


halo_coords = final_snap.halo_coordinates
halo_mass = cat.masses.mass_200crit
struc = cat.structure_type.structuretype 
halo_coords = halo_coords[numpy.where(struc == 10)[0]]
halo_mass = halo_mass[numpy.where(struc == 10)[0]]
halo_coords = halo_coords[numpy.where(halo_mass > 0)[0]]
halo_mass = halo_mass[numpy.where(halo_mass > 0)[0]]
halo_mass.convert_to_units('msun')

boxsize = final_snap.boxsize
boxsize.to(final_snap.gas.coordinates.units)


ball_radius = 4

tree = cKDTree(halo_coords, boxsize = boxsize.value)
print('searching')
nearby_halos = tree.query_ball_point(gas_coords, ball_radius, n_jobs = -1)
print('searched')
nearby_halo_density = numpy.empty(len(nearby_halos))
for i in range(len(nearby_halos)):
    indices = numpy.array(nearby_halos[i])
    indices = indices.astype(int)
    nearby_halo_mass = halo_mass[indices]
    total_mass = numpy.sum(nearby_halo_mass)
    nearby_halo_density[i] = (3*total_mass)/(4*numpy.pi*ball_radius**3)
    if i in numpy.arange(0,6000000, 100000):
        print(i)
    

print(numpy.amin(nearby_halo_density))
'''
numpy.savetxt('/cosma5/data/durham/dc-murr1/gas_neighbour_density.txt', nearby_halo_density)
'''






