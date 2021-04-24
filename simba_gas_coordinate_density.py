import numpy 
import unyt
import hist
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib.colors import LogNorm
pyplot.rcParams.update({'font.size':40})
from transfer.frontends.simbaahf import SIMBASnapshotData

initial_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_000.hdf5', halo_filename = None)

truncate_ids = {
 0: initial_snap.gas.particle_ids.max() + 1,
 1: None,
 4: initial_snap.gas.particle_ids.max() + 1,
}

final = SIMBASnapshotData(
    '/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_151.hdf5',
    '/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos',
    truncate_ids = truncate_ids
)
z_halos = final.halo_coordinates[:,2]
z_halos.convert_to_units('Mpc')
z_massive = z_halos[0]

coords = final.gas.coordinates
coords.convert_to_units('Mpc')
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
    '/cosma5/data/durham/dc-murr1/simba_gas_coordinate_density.png',
    73
)
'''