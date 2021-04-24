import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib.colors import LogNorm
from velociraptor import load
import unyt
pyplot.rcParams.update({'font.size':40})

nearest_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halos.txt')
neighbour_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_neighbour_halos.txt')
mask = numpy.where(neighbour_halos != -1)[0]
nearest_halos = nearest_halos[mask]
neighbour_halos = neighbour_halos[mask]
nearest_halos = nearest_halos.astype(int)
neighbour_halos = neighbour_halos.astype(int)

cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
masses = cat.masses.mass_200crit
masses.convert_to_units('msun')

nearest_mass = masses[nearest_halos]
neighbour_mass = masses[neighbour_halos]

where1 = numpy.where(nearest_mass > 0)[0]
nearest_mass = nearest_mass[where1]
neighbour_mass = neighbour_mass[where1]

where2 = numpy.where(neighbour_mass > 0)[0]
nearest_mass = nearest_mass[where2]
neighbour_mass = neighbour_mass[where2]

xbins = numpy.logspace(numpy.log10(numpy.amin(nearest_mass)), numpy.log10(numpy.amax(nearest_mass)), 50)
ybins = numpy.logspace(numpy.log10(numpy.amin(neighbour_mass)), numpy.log10(numpy.amax(neighbour_mass)), 50)

ref = [10**8, 10**13]

simba_nearest_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/simba_gas_nearest_halos.txt')
simba_neighbour_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/simba_gas_neighbour_halos.txt')
simba_mask = numpy.where(simba_neighbour_halos != -1)[0]
simba_nearest_halos = simba_nearest_halos[mask]
simba_neighbour_halos = simba_neighbour_halos[mask]
simba_nearest_halos = simba_nearest_halos.astype(int)
simba_neighbour_halos = simba_neighbour_halos.astype(int)

simba_masses = unyt.unyt_array(numpy.genfromtxt('/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos', usecols = 3).T, units = unyt.msun / 0.7)
simba_masses.convert_to_units('msun')

simba_nearest_mass = simba_masses[nearest_halos]
simba_neighbour_mass = simba_masses[neighbour_halos]

simba_where1 = numpy.where(simba_nearest_mass > 0)[0]
simba_nearest_mass = simba_nearest_mass[simba_where1]
simba_neighbour_mass = simba_neighbour_mass[simba_where1]

simba_where2 = numpy.where(simba_neighbour_mass > 0)[0]
simba_nearest_mass = simba_nearest_mass[simba_where2]
simba_neighbour_mass = simba_neighbour_mass[simba_where2]

simba_xbins = numpy.logspace(numpy.log10(numpy.amin(simba_nearest_mass)), numpy.log10(numpy.amax(simba_nearest_mass)), 50)
simba_ybins = numpy.logspace(numpy.log10(numpy.amin(simba_neighbour_mass)), numpy.log10(numpy.amax(simba_neighbour_mass)), 50)


fig, (ax1, ax2) = pyplot.subplots(1, 2, figsize = (40, 20))
ax1.hist2d(nearest_mass, neighbour_mass, bins = [xbins, ybins], norm = LogNorm())
ax1.loglog()
ax1.plot(xbins, xbins, linestyle = '-', linewidth = 4, color = 'red')

ax2.hist2d(simba_nearest_mass, simba_neighbour_mass, bins = [simba_xbins, simba_ybins], norm = LogNorm())
ax2.loglog()
ax2.plot(simba_xbins, simba_xbins, linestyle = 'dashdot', linewidth = 4, color = 'red')

fig.add_subplot(111, frame_on=False)
pyplot.tick_params(labelcolor="none", bottom=False, left=False)

pyplot.ylabel(r"Neighbour halo mass [M$_\odot$]", labelpad = 20)
pyplot.xlabel(r"Nearest halo mass [M$_\odot$]")
fig.savefig('/cosma5/data/durham/dc-murr1/nearest_vs_neighbour.png')
