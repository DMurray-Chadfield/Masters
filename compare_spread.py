import numpy
import matplotlib
from matplotlib import pyplot

pyplot.rcParams.update({'font.size':40})

gas = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt')
dm = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_spread.txt')
star = numpy.loadtxt('/cosma5/data/durham/dc-murr1/star_spread.txt')

gas_hist, gas_edges = numpy.histogram(gas, bins = 100, density = True)
dm_hist, dm_edges = numpy.histogram(dm, bins = 100, density = True)
star_hist, star_edges = numpy.histogram(star, bins = 100, density = True)

gas_centers = numpy.zeros(len(gas_edges)-1)
dm_centers = numpy.zeros(len(dm_edges)-1)
star_centers = numpy.zeros(len(star_edges)-1)

for i in range(len(gas_centers)):
    gas_centers[i] = (gas_edges[i] + gas_edges[i+1])/2
for i in range(len(dm_centers)):
    dm_centers[i] = (dm_edges[i] + dm_edges[i+1])/2
for i in range(len(star_centers)):
    star_centers[i] = (star_edges[i] + star_edges[i+1])/2

fig, ax = pyplot.subplots(figsize = (20,20))
ax.plot(dm_centers, dm_hist, label = 'Dark Matter', linewidth = 5)
ax.plot(gas_centers, gas_hist, label = 'Gas', linewidth = 5)
ax.plot(star_centers, star_hist, label = 'Stars', linewidth = 5)
ax.legend()
ax.set_yscale('log')
ax.set_ylabel('Probability density')
ax.set_xlabel('Spread metric [Mpc]')
fig.savefig('/cosma5/data/durham/dc-murr1/ref_spread.png')