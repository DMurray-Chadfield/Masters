import numpy
from velociraptor import load
from numba import njit

halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/nearest_halos.txt')
halos = halos.astype(int)
halo_coords = numpy.loadtxt('/cosma5/data/durham/dc-murr1/halos.txt', usecols = (0,1,2))
cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
masses = cat.masses.mass_200crit
struc = cat.structure_type.structuretype 
halo_coords = halo_coords[numpy.where(struc == 10)[0], :]
masses = masses[numpy.where(struc == 10)[0]]
halo_coords = halo_coords[numpy.where(masses > 0)[0], :]
masses = masses[numpy.where(masses > 0)[0]]
masses.convert_to_units('msun')
dm_coords = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_particle_coordinates.txt')

@njit
def find_dipoles(part_pos, halo_pos, halo_masses):
    dipoles = numpy.zeros(len(part_pos))
    
    for i in range(len(dipoles)):
        coords = halo_coords[halos[i,:], :]
        part_coord = part_pos[i,:]
        
        vectors = numpy.subtract(coords, part_coord)
        for p in range(10):
            for q in range(3):
                if numpy.absolute(vectors[p,q]) > 20:
                    if vectors[p,q] > 0:
                        vectors[p,q] -= 25
                    else:
                        vectors[p,q] += 25
        
        mass = masses[halos[i,:]]

        dipole_vecs = numpy.zeros((10,3))
        for p in range(10):
            for q in range(3):
                dipole_vecs[p,q] = mass[p]*vectors[p*q]
        
        dipole_vec = numpy.zeros(3)
        for q in range(3):
            dipole_vec[q] = numpy.sum(dipole_vecs[:,q])
        
        dipoles[i] = numpy.sqrt(dipole_vec[0]**2 + dipole_vec[1]**2 + dipole_vec[2]**2)
    
    return dipoles


dipoles = find_dipoles(dm_coords, halo_coords, masses)
numpy.savetxt('/cosma5/data/durham/dc-murr1/dipoles.txt', dipoles)

         

