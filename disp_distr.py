import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy

disp = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_displacements.txt')
hist, bin_edges = numpy.histogram(disp, bins = 1000, density = True)

bin_centers = numpy.zeros(len(bin_edges) - 1)
for i in range(len(bin_centers)):
    bin_centers[i] = (bin_edges[i] + bin_edges[i+1])/2

fig, ax = pyplot.subplots()
ax.plot(bin_centers, hist)
ax.set_yscale('log')
fig.savefig('/cosma5/data/durham/dc-murr1/disp_distr.png')
