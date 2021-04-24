from velociraptor.particles import load_groups
from velociraptor import load
from velociraptor.swift.swift import to_swiftsimio_dataset
import numpy
import unyt

catalogue = load("/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties")
groups = load_groups("/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.catalog_groups", catalogue=catalogue)

struc = catalogue.structure_type.structuretype
n = len(struc[struc == 10])
radii = catalogue.apertures.rhalfmass_star_30_kpc
masses = catalogue.apertures.mass_star_30_kpc
radii.convert_to_units(unyt.kpc)
masses.convert_to_units(unyt.msun)


data = numpy.zeros((n, 5))
ids = numpy.where(struc == 10)[0]
data[:,0] = catalogue.positions.xc[ids]
data[:,1] = catalogue.positions.yc[ids]
data[:,2] = catalogue.positions.zc[ids]
data[:,3] = radii[ids]
data[:,4] = masses[ids]

numpy.savetxt('/cosma5/data/durham/dc-murr1/halos.txt', data)
