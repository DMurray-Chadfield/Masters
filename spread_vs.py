import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib.colors import LogNorm

spreads = numpy.loadtxt('/cosma5/data/durham/dc-murr1/bound_dm_spread.txt')
masses = numpy.loadtxt('/cosma5/data/durham/dc-murr1/halo_masses.txt')
radii = numpy.loadtxt('/cosma5/data/durham/dc-murr1/halo_radii.txt')
masses = masses*10**10

fig, (ax1, ax2) = pyplot.subplots(1, 2, sharey = True)

h1 = ax1.hist2d(masses, spreads, bins = 1000, norm = LogNorm())
fig.colorbar(h1[3], ax = ax1)
h2 = ax2.hist2d(radii, spreads, bins = 1000, norm = LogNorm())
fig.colorbar(h2[3], ax = ax2)
ax1.loglog()
ax2.loglog()
ax1.set_ylabel('DM Particle Spread Metric [Mpc]')
ax1.set_xlabel("Mass of particle's halo [$M_{\odot}$]")
ax2.set_xlabel("Radius of particle's halo [Mpc]")
fig.savefig('/cosma5/data/durham/dc-murr1/spread_vs.png')