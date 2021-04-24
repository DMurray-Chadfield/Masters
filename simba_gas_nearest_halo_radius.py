from transfer.frontends.simbaahf import SIMBASnapshotData
import unyt
import numpy

initial_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_000.hdf5', halo_filename = None)

truncate_ids = {
 0: initial_snap.gas.particle_ids.max() + 1,
 1: None,
 4: initial_snap.gas.particle_ids.max() + 1,
}

final_snap = SIMBASnapshotData('/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_151.hdf5', 
halo_filename = '/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos', truncate_ids = truncate_ids)

radii = final_snap.halo_radii
radii.convert_to_units('Mpc')

halo_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/simba_gas_nearest_halos.txt')
halo_ids = halo_ids.astype(int)

halo_radii = radii[halo_ids]

numpy.savetxt('/cosma5/data/durham/dc-murr1/simba_gas_nearest_halo_radius.txt', halo_radii)