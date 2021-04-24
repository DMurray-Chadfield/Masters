from velociraptor.particles import load_groups
from velociraptor import load
from velociraptor.swift.swift import to_swiftsimio_dataset
import numpy
import unyt

catalogue = load('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties')




data = numpy.zeros((len(catalogue.positions.xc), 3))

data[:,0] = catalogue.positions.xc
data[:,1] = catalogue.positions.yc
data[:,2] = catalogue.positions.zc


numpy.savetxt('/cosma5/data/durham/dc-murr1/adi_halo_coords.txt', data)