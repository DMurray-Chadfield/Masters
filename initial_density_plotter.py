from swiftsimio import load
from swiftsimio.visualisation.projection import project_gas

data = load("/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0000.hdf5")


# This creates a grid that has units msun / Mpc^2, and can be transformed like
# any other unyt quantity
mass_map = project_gas(data, resolution=1024, project="masses", parallel=True)


# Let's say we wish to save it as msun / kpc^2,
#from unyt import msun, kpc
#mass_map.convert_to_units(msun / kpc**2)

from matplotlib.pyplot import imsave
from matplotlib.colors import LogNorm

# Normalize and save
imsave("/cosma5/data/durham/dc-murr1/initial_gas_density_projection.pdf", LogNorm()(mass_map.value), cmap="copper")