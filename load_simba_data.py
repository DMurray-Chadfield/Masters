import h5py
import numpy

data = h5py.File('/cosma6/data/dp004/dc-borr1/simba-runs/s50j7k/snap_m50n512_151.hdf5', 'r')

id = numpy.array(data['PartType4']['ParticleIDs'])
print(numpy.amin(id), numpy.amax(id))