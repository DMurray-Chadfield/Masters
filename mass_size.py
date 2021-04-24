import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy
from velociraptor.tools.labels import get_full_label
from velociraptor import load
from unyt import msun
from unyt import Mpc
from velociraptor.tools.lines import binned_median_line as bml
import unyt

pyplot.rcParams.update({'font.size':40})

data = numpy.loadtxt('/cosma5/data/durham/dc-murr1/halos.txt')
units = load("/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties")
masses = units.apertures.mass_star_30_kpc
radii = units.apertures.rhalfmass_star_30_kpc
masses.convert_to_units(unyt.msun)
radii.convert_to_units(unyt.kpc)
xlabel = get_full_label(masses)
ylabel = get_full_label(radii)

r = data[:,3]
m = data[:,4]

r = r[numpy.where(m > 0)[0]]
m = m[numpy.where(m > 0)[0]]

mass_bins = numpy.logspace(numpy.log10(numpy.min(m)),numpy.log10(numpy.max(m)), 10)
mass_bins = unyt.unyt_array(mass_bins, units = unyt.msun)
m = unyt.unyt_array(m, units = unyt.msun)
r = unyt.unyt_array(r, units = unyt.kpc)
centers, med, err = bml(m, r, mass_bins, minimum_in_bin = 1)

fig, ax = pyplot.subplots(figsize = (20,20))
ax.scatter(m, r, marker = 'o', s = 64, color = 'blue', alpha = 0.3)
ax.plot(centers, med, color = 'blue', linestyle = '--', linewidth = 6, label = 'EAGLE')
ax.loglog()
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)

obs = numpy.loadtxt('/cosma5/data/durham/dc-murr1/Trujillo2020.txt', delimiter = ',')

m_obs = obs[:,0]
r_obs = obs[:,1]
obs_bins = numpy.logspace(numpy.log10(numpy.min(m_obs)),numpy.log10(numpy.max(m_obs)), 10)
obs_bins = unyt.unyt_array(obs_bins, units = unyt.msun)
m_obs = unyt.unyt_array(m_obs, units = unyt.msun)
r_obs = unyt.unyt_array(r_obs, units = unyt.kpc)
obs_centers, obs_med, obs_err = bml(m_obs, r_obs, obs_bins, minimum_in_bin = 1)

ax.scatter(m_obs, r_obs, marker = 'o', s = 64, color = 'red', alpha = 0.3)
ax.plot(obs_centers, obs_med, color = 'red', linestyle = '--', linewidth = 6, label = 'Trujillo et al.')

ax.legend()
fig.savefig('/cosma5/data/durham/dc-murr1/mass_size.png')
