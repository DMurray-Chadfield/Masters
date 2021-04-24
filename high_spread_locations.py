import numpy
from swiftsimio import load
import unyt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from swiftsimio.visualisation.projection import scatter_parallel
from matplotlib.colors import LogNorm

snap = load('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5')


spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt')

where = numpy.where(spread > 1)[0]
coords = snap.gas.coordinates
masses = snap.gas.masses
smooth = snap.gas.smoothing_lengths
coords = coords[where,:]
masses = masses[where]
smooth = smooth[where]
masses.convert_to_units('msun')

coords = coords/25

x = coords[:,0]
y = coords[:,1]

map = scatter_parallel(x=x, y=y, h=smooth, m=masses, res=1024)

pyplot.imsave('/cosma5/data/durham/dc-murr1/high_spread_projection.png', LogNorm()(map), cmap = 'copper')