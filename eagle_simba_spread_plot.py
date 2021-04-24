import h5py
import unyt
import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
import h5py

eagle_gas = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt')
eagle_dm = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_spread.txt')
adi_gas = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adiabatic_gas_spread.txt')
adi_dm = numpy.loadtxt('/cosma5/data/durham/dc-murr1/adiabatic_dm_spread.txt')
simba_gas = unyt.unyt_array(h5py.File('/cosma5/data/durham/dc-murr1/gas_spread.hdf5', 'r')['array_data'], units = 1/0.7 * unyt.kpc)
simba_dm = unyt.unyt_array(h5py.File('/cosma5/data/durham/dc-murr1/dark_matter_spread.hdf5', 'r')['array_data'], units = 1/0.7 * unyt.kpc)
simba_gas.convert_to_units('Mpc')
simba_dm.convert_to_units('Mpc')

n = 50

adi_gas_hist, adi_gas_edges = numpy.histogram(adi_gas, bins = n, density = True)
adi_gas_centers = numpy.empty(len(adi_gas_edges) - 1)

adi_dm_hist, adi_dm_edges = numpy.histogram(adi_dm, bins = n, density = True)
adi_dm_centers = numpy.empty(len(adi_dm_edges) - 1)

eagle_gas_hist, eagle_gas_edges = numpy.histogram(eagle_gas, bins = n, density = True)
eagle_gas_centers = numpy.empty(len(eagle_gas_edges) - 1)

eagle_dm_hist, eagle_dm_edges = numpy.histogram(eagle_dm, bins = n, density = True)
eagle_dm_centers = numpy.empty(len(eagle_dm_edges) - 1)

simba_gas_hist, simba_gas_edges = numpy.histogram(simba_gas, bins = n, density = True)
simba_gas_centers = numpy.empty(len(simba_gas_edges) - 1)

simba_dm_hist, simba_dm_edges = numpy.histogram(simba_dm, bins = n, density = True)
simba_dm_centers = numpy.empty(len(simba_dm_edges) - 1)

for i in range(n):
    adi_gas_centers[i] = (adi_gas_edges[i] + adi_gas_edges[i+1])/2
    adi_dm_centers[i] = (adi_dm_edges[i] + adi_dm_edges[i+1])/2
    eagle_gas_centers[i] = (eagle_gas_edges[i] + eagle_gas_edges[i+1])/2
    eagle_dm_centers[i] = (eagle_dm_edges[i] + eagle_dm_edges[i+1])/2
    simba_gas_centers[i] = (simba_gas_edges[i] + simba_gas_edges[i+1])/2
    simba_dm_centers[i] = (simba_dm_edges[i] + simba_dm_edges[i+1])/2

fig, ax = pyplot.subplots(figsize = (20,20))
ax.plot(adi_gas_centers, adi_gas_hist, linestyle = '--', linewidth = 6, color = 'orange', label = 'Adiabatic Gas')
ax.plot(adi_dm_centers, adi_dm_hist, linestyle = '--', linewidth = 6, color = 'blue', label = 'Adiabatic Dark Matter')
ax.plot(eagle_gas_centers, eagle_gas_hist, linewidth = 6, color = 'orange', label = 'EAGLE Gas')
ax.plot(eagle_dm_centers, eagle_dm_hist, linewidth = 6, color = 'blue', label = 'EAGLE Dark Matter')
ax.plot(simba_gas_centers, simba_gas_hist, linestyle = 'dashdot', linewidth = 6, color = 'orange', label = 'SIMBA Gas')
ax.plot(simba_dm_centers, simba_dm_hist, linestyle = 'dashdot', linewidth = 6, color = 'blue', label = 'SIMBA Dark Matter')
ax.set_yscale('log')
ax.legend(loc = 'upper right')
ax.tick_params(which = 'both', direction = 'in')
ax.tick_params(length = 10, width = 2)
ax.set_xlabel('Spread Metric [Mpc]')
ax.set_ylabel('Probability density')
fig.savefig('/cosma5/data/durham/dc-murr1/eagle_simba_adi_spread_plot.png')