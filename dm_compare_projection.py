import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import dm_projection
import dm_blob_projection
from matplotlib.colors import LogNorm

blob_map = dm_blob_projection.map
dm_map = dm_projection.dm_mass

fig, (ax1, ax2) = pyplot.subplots(1, 2, figsize = (40, 20))
ax1.imshow(LogNorm()(blob_map), cmap = 'inferno')
ax2.imshow(LogNorm()(dm_map), cmap = 'inferno')
ax1.set_axis_off()
ax2.set_axis_off()
fig.savefig('/cosma5/data/durham/dc-murr1/dm_compare_projection.png')