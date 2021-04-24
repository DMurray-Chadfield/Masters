from velociraptor import load
from velociraptor.particles import load_groups
import numpy

groups = load_groups('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.catalog_groups')

particles, unbound_particles = groups.extract_halo(halo_id = 1)

print(numpy.where(particles.particle_types == 2))
