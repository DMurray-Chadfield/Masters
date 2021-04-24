import numpy
from velociraptor.particles import load_groups
from velociraptor import load
from velociraptor.swift.swift import to_swiftsimio_dataset
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

catalogue = load("/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties")
groups = load_groups("/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.catalog_groups", catalogue=catalogue)

particles, unbound_particles = groups.extract_halo(halo_id = 2000)

data, mask = to_swiftsimio_dataset(
    particles,
    "/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5",
    generate_extra_mask=True
)

a = data.stars.birth_scale_factors
z = 1/a - 1
bins = numpy.logspace(numpy.log10(numpy.amin(z)), numpy.log10(numpy.amax(z)), 20)
hist, bin_edges = numpy.histogram(z, bins = bins, density = True)
bin_centers = numpy.empty(len(hist))
for i in range(len(bin_centers)):
    bin_centers[i] = (bin_edges[i] + bin_edges[i+1])/2

fig, ax = pyplot.subplots(figsize = (20,20))
ax.plot(bin_centers, hist)
ax.set_xscale('log')
ax.invert_xaxis()
fig.savefig('/cosma5/data/durham/dc-murr1/halo_sfhistory.png')