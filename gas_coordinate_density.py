import numpy 
import unyt
import hist
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib.colors import LogNorm
pyplot.rcParams.update({'font.size':40})
from transfer.frontends.swiftvr import SWIFTSnapshotData

final = SWIFTSnapshotData('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5',
halo_filename = '/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
z_halos = final.halo_coordinates[:,2]
z_halos.convert_to_units('Mpc')
z_massive = z_halos[0]

coords = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_coords.txt'), units ='Mpc')
x = coords[:,0]
y = coords[:,1]
z = coords[:,2]

where = numpy.where(numpy.logical_and(z > z_massive.value - 0.5, z < z_massive.value + 0.5))[0]
x = x[where]
y = y[where]

'''
hist.lin_hist(
    x,
    y,
    'x coordinate [Mpc]',
    'y coordinate [Mpc]',
    '/cosma5/data/durham/dc-murr1/gas_coordinate_density.png',
    25
)
'''