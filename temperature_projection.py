from swiftsimio import load
from swiftsimio.visualisation.projection import project_gas

data = load("/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5")

# First create a mass-weighted temperature dataset
data.gas.mass_weighted_temps = data.gas.masses * data.gas.temperatures

# Map in msun / mpc^2
mass_map = project_gas(data, resolution=1024, project="masses", parallel=True)
# Map in msun * K / mpc^2
mass_weighted_temp_map = project_gas(
    data,
    resolution=1024,
    project="mass_weighted_temps",
    parallel=True
)

temp_map = mass_weighted_temp_map / mass_map

from unyt import K
temp_map.convert_to_units(K)

from matplotlib.pyplot import imsave
from matplotlib.colors import LogNorm

# Normalize and save
imsave("/cosma5/data/durham/dc-murr1/temp_map.png", LogNorm()(temp_map.value), cmap="hot")