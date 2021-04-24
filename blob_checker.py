import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib.colors import LogNorm
from velociraptor import load

spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adiabatic_gas_spread.txt')
halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_neighbour_halos.txt')

mask = numpy.where(halos != -1)[0]
spread = spread[mask]
halos = halos[mask]
print(halos, len(halos))
cat = load('/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties')
masses = cat.masses.mass_200crit
masses.convert_to_units('msun')

halos = halos.astype(int)
halo_masses = masses[halos]
print(halo_masses, len(halo_masses))
where = numpy.where(halo_masses > 0)[0]
halo_masses = halo_masses[where]
spread = spread[where]

print(halo_masses, len(halo_masses))

xbins = numpy.logspace(numpy.log10(numpy.amin(halo_masses)), numpy.log10(numpy.amax(halo_masses)), 50)
ybins = numpy.logspace(numpy.log10(numpy.amin(spread)), numpy.log10(numpy.amax(spread)), 50)

fig, ax = pyplot.subplots()
ax.hist2d(halo_masses, spread, bins = [xbins, ybins], norm = LogNorm())
ax.loglog()
fig.savefig('/cosma5/data/durham/dc-murr1/blob_checker.png')