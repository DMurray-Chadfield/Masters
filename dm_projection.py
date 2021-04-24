from swiftsimio import load
from swiftsimio.visualisation.projection import project_pixel_grid
from swiftsimio.visualisation.smoothing_length_generation import generate_smoothing_lengths
from swiftsimio.visualisation.projection import scatter_parallel

data = load("/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5")

# Generate smoothing lengths for the dark matter
data.dark_matter.smoothing_lengths = generate_smoothing_lengths(
    data.dark_matter.coordinates,
    data.metadata.boxsize,
    kernel_gamma=1.8,
    neighbours=57,
    speedup_fac=2,
    dimension=3,
)

# Project the dark matter mass
dm_mass = project_pixel_grid(
    # Note here that we pass in the dark matter dataset not the whole
    # data object, to specify what particle type we wish to visualise
    data=data.dark_matter,
    boxsize=data.metadata.boxsize,
    resolution=1024,
    project="masses",
    parallel=True,
    region=None
)


#dm_mass = scatter_parallel(x=data.dark_matter.coordinates[0], y=data.dark_matter.coordinates[1], h= data.dark_matter.smoothing_lengths, m=data.dark_matter.masses, res=1024)

from matplotlib.pyplot import imsave
from matplotlib.colors import LogNorm

# Everyone knows that dark matter is purple
imsave("/cosma5/data/durham/dc-murr1/dm_projection.png", LogNorm()(dm_mass), cmap="inferno")