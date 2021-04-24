from transfer.frontends.swiftvr import SWIFTSnapshotData
import unyt
import numpy
from velociraptor import load


cat = load('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties')
radii = cat.radii.r_200crit
radii.convert_to_units('Mpc')

halo_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halos.txt')
halo_ids = halo_ids.astype(int)

halo_radii = radii[halo_ids]

numpy.savetxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halo_radius.txt', halo_radii)