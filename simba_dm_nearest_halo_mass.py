import unyt
import numpy

masses = unyt.unyt_array(numpy.genfromtxt('/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos', usecols = 3).T, units = 1/0.7 * unyt.msun)
masses.convert_to_units('msun')

halo_ids = numpy.loadtxt('/cosma5/data/durham/dc-murr1/simba_dm_nearest_halos.txt')
halo_ids = halo_ids.astype(int)

halo_masses = masses[halo_ids]

numpy.savetxt('/cosma5/data/durham/dc-murr1/simba_dm_nearest_halo_mass.txt', halo_masses)