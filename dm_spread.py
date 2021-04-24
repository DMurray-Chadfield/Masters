from velociraptor import load
from velociraptor.particles import load_groups
import numpy
from gaussian import distribute_particles
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

data = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

tot = data.number.gas + data.number.bh + data.number.star
part = data.number.part
dm = part - tot
radii = data.radii.rvir


halos = []
spread = numpy.array([])
for i in range(len(dm)):   
    halos.append(distribute_particles(dm[i], radii[i]))
    spread = numpy.append(spread, halos[i].spreads)

n_bins = 100

g_hist, g_bin_edges = numpy.histogram(spread, n_bins, density = True)
g_bin_centers = numpy.zeros(len(g_hist))

for i in range(len(g_bin_centers)):
    g_bin_centers[i] = (g_bin_edges[i] + g_bin_edges[i+1])/2


dm_spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_spread.txt')
gas_spread = numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_spread.txt')
disp = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_displacements.txt')
x = numpy.loadtxt('/cosma5/data/durham/dc-murr1/ids.txt')
bound_dm_spread = dm_spread[numpy.where(x >= 0)]
unbound_dm_spread = dm_spread[numpy.where(x < 0)]


bound_dm_hist, bound_dm_bin_edges = numpy.histogram(bound_dm_spread, n_bins, density = True)
bound_dm_bin_centers = numpy.zeros(len(bound_dm_hist))
for i in range(len(bound_dm_bin_centers)):
    bound_dm_bin_centers[i] = (bound_dm_bin_edges[i] + bound_dm_bin_edges[i+1])/2

unbound_dm_hist, unbound_dm_bin_edges = numpy.histogram(unbound_dm_spread, n_bins, density = True)
unbound_dm_bin_centers = numpy.zeros(len(unbound_dm_hist))
for i in range(len(unbound_dm_bin_centers)):
    unbound_dm_bin_centers[i] = (unbound_dm_bin_edges[i] + unbound_dm_bin_edges[i+1])/2

gas_hist, gas_bin_edges = numpy.histogram(gas_spread, n_bins, density = True)
gas_bin_centers = numpy.zeros(len(gas_hist))
for i in range(len(gas_bin_centers)):
    gas_bin_centers[i] = (gas_bin_edges[i] + gas_bin_edges[i+1])/2

disp_hist, disp_bin_edges = numpy.histogram(disp, n_bins, density = True)
disp_bin_centers = numpy.zeros(len(disp_hist))
for i in range(len(disp_bin_centers)):
    disp_bin_centers[i] = (disp_bin_edges[i] + disp_bin_edges[i+1])/2

fig, ax1 = pyplot.subplots()
ax1.plot(bound_dm_bin_centers, bound_dm_hist, label = 'Inside Haloes')
ax1.plot(unbound_dm_bin_centers, unbound_dm_hist, label = 'Outside Haloes')
ax1.plot(g_bin_centers, g_hist, label = 'Gaussian')
ax1.plot(disp_bin_centers, disp_hist, label = 'Displacements')
ax1.set_yscale('log')
ax1.set_xlabel('Dark Matter Spread Metric [Mpc]')


axins = ax1.inset_axes([0.5, 0.5, 0.47, 0.47])
axins.plot(bound_dm_bin_centers, bound_dm_hist)
axins.plot(unbound_dm_bin_centers, unbound_dm_hist)
axins.plot(g_bin_centers, g_hist)
axins.plot(disp_bin_centers, disp_hist)
x1, x2, y1, y2 = 0, 1, 1, 10
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.set_xticklabels('')
axins.set_yticklabels('')
ax1.legend(loc='lower left')
ax1.indicate_inset_zoom(axins)


fig.savefig('/cosma5/data/durham/dc-murr1/gaussian_observed_dm.png')

