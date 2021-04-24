from matplotlib import pyplot
from matplotlib.patches import Circle
import matplotlib
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
matplotlib.use('Agg')
import numpy
from velociraptor import load
import unyt

image = pyplot.imread('/cosma5/data/durham/dc-murr1/low_spread_projection.png')
data = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

struc = data.structure_type.structuretype
xc = data.positions.xc
yc = data.positions.yc
zc = data.positions.zc
radii = data.radii.r_200crit
masses = data.masses.mass_200crit

radii.convert_to_units('Mpc')
masses.convert_to_units('msun')

mask = numpy.where(struc == 10)[0]
xc = xc[mask]
yc = yc[mask]
zc = zc[mask]
radii = radii[mask]
masses = masses[mask]

fig, ax = pyplot.subplots(1, frameon = False)
fig.set_size_inches(10,10)
image = numpy.transpose(image, axes = (1,0,2))
ax.imshow(image, extent = [0,25,0,25], origin = 'lower', )

n = len(xc)
hot = cm.get_cmap('hot', n)
colors = hot(range(n))

bins = [8,9,10,11,12,13]
sort_masses = numpy.sort(masses)
maxm = numpy.amax(masses)
minm = numpy.amin(numpy.abs(masses))

for i in range(n): 
    x = xc[i]
    y = yc[i]
    z = zc[i]
    rad = radii[i]
    m = masses[i]
    if rad < 0 or m < 0:
        pass
    else:
        mbin = numpy.round(numpy.log10(m))
        w = numpy.where(sort_masses == m)[0]
        c_cont = tuple(colors[w][0:3])[0]
        j = numpy.where(bins == mbin)[0]
        c = tuple(colors[j][0:3])
        trans = unyt.unyt_quantity(1, 1000 * unyt.kpc) - z/25
        ax.add_patch(Circle((x,y), radius = rad, fill = False, color = c_cont, alpha = float(trans.value)))

ax.set_axis_off()

fig.savefig('/cosma5/data/durham/dc-murr1/low_circled.png')