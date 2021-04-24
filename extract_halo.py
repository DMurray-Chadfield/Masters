from velociraptor.particles import load_groups
from velociraptor import load
from velociraptor.swift.swift import to_swiftsimio_dataset
from swiftsimio.visualisation.sphviewer import SPHViewerWrapper
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm

catalogue = load("/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.properties")
groups = load_groups("/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/halo_0007.catalog_groups", catalogue=catalogue)

particles, unbound_particles = groups.extract_halo(halo_id=0)

data, mask = to_swiftsimio_dataset(
    particles,
    "/cosma6/data/dp004/dc-borr1/snap7/new_randomness_runs/adiabatic/Run_0/eagle_0007.hdf5",
    generate_extra_mask=True
)


particle_data = getattr(data, 'dark_matter')
sphviewer = SPHViewerWrapper(particle_data)

x = particles.x / data.metadata.a
y = particles.y / data.metadata.a
z = particles.z / data.metadata.a
r_size = particles.r_size * 0.8 / data.metadata.a

sphviewer.get_camera(x=x, y=y, z=z, r=r_size, zoom=2, xsize=1024, ysize=1024)
sphviewer.get_scene()
sphviewer.get_render()

fig, ax = plt.subplots(figsize=(8, 8), dpi=1024 // 8)
fig.subplots_adjust(0, 0, 1, 1)
ax.axis("off")

ax.imshow(sphviewer.image.value, norm = LogNorm(), cmap="plasma", origin="lower")


fig.savefig("/cosma5/data/durham/dc-murr1/singular_halo.png")
