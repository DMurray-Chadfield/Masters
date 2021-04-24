import numpy 
import unyt
from swiftsimio import load
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from swiftsimio.visualisation.projection import scatter_parallel
import project
from matplotlib.colors import LogNorm
from swiftsimio.visualisation.smoothing_length_generation import generate_smoothing_lengths

spread = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_spread.txt'), units = 'Mpc')
halo_mass = unyt.unyt_array(numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_nearest_halo_mass.txt'), units = 'msun')
dm_halos = numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_neighbour_halos.txt')
dm_halos = dm_halos.astype(int)
snap = load('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5')
coords = snap.dark_matter.coordinates
masses = snap.dark_matter.masses
smooth = generate_smoothing_lengths(
    coords,
    snap.metadata.boxsize,
    kernel_gamma=1.8,
    neighbours=57,
    speedup_fac=2,
    dimension=3,
)

mask = numpy.where(halo_mass > 0)[0]
spread = spread[mask]
halo_mass = halo_mass[mask]
dm_halos = dm_halos[mask]
coords = coords[mask]
masses = masses[mask]
smooth = smooth[mask]

where = numpy.where(dm_halos >= 0)[0]
spread = spread[where]
halo_mass = halo_mass[where]
coords = coords[where]
masses = masses[where]
smooth = smooth[where]

mass_cutoff = numpy.where(numpy.logical_and(halo_mass > 10**8, halo_mass < 10**10))[0]
spread = spread[mass_cutoff]
coords = coords[mass_cutoff]
masses = masses[mass_cutoff]
smooth = smooth[mass_cutoff]

spread_cutoff = numpy.where(numpy.logical_and(spread > 10**(-1), spread < 1))[0]
coords = coords[spread_cutoff]
masses = masses[spread_cutoff]
smooth = smooth[spread_cutoff]

#coords = coords/25

#x = coords[:,0]
#y = coords[:,1]

map = project.project_pixel_grid(
    coords = coords, smooth = smooth, masses = masses, boxsize = snap.metadata.boxsize, resolution = 1024, project = 'masses', parallel = True, region = None
    )

pyplot.imsave('/cosma5/data/durham/dc-murr1/dm_blob_projection.png', LogNorm()(map), cmap = 'inferno')