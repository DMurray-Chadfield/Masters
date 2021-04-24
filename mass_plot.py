from velociraptor import load
from velociraptor.tools.labels import get_full_label
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
from velociraptor.tools.lines import binned_median_line as bml
import numpy
import unyt
from velociraptor.tools.labels import get_full_label

data = load("/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties")

stellar_mass = data.masses.m_star_30kpc
halo_mass = data.masses.mass_200crit
s_wh = numpy.where(stellar_mass > 0)[0]
stellar_mass = stellar_mass[s_wh]
halo_mass = halo_mass[s_wh]
h_wh = numpy.where(halo_mass > 0)
stellar_mass = stellar_mass[h_wh]
halo_mass = halo_mass[h_wh]


stellar_mass.convert_to_units('msun')
halo_mass.convert_to_units('msun')

mass_bins = numpy.logspace(numpy.log10(numpy.min(stellar_mass).value), numpy.log10(numpy.max(stellar_mass).value), 10)
mass_bins = unyt.unyt_array(mass_bins, units = stellar_mass.units)
centers, med, err = bml(stellar_mass, halo_mass, mass_bins, minimum_in_bin = 1)

obs = numpy.loadtxt('/cosma5/data/durham/dc-murr1/Behroozi2013.txt')
h_obs = unyt.unyt_array(10**obs[:,0], units = unyt.msun)
s_obs = unyt.unyt_array((10**obs[:,1])*h_obs, units = unyt.msun)
obs_bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.min(s_obs).value), numpy.log10(numpy.max(s_obs).value), 10), units = unyt.msun)
obs_centers, obs_med, obs_err = bml(s_obs, h_obs, obs_bins, minimum_in_bin = 1)

xlabel = get_full_label(stellar_mass)
ylabel = get_full_label(halo_mass)

fig, ax = pyplot.subplots(figsize = (20,20))
ax.loglog()
ax.scatter(stellar_mass, halo_mass, s = 64, alpha = 0.2, color = 'blue')
ax.plot(centers, med, linestyle = '--', linewidth = 6, color = 'blue', label = 'EAGLE')
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
ax.scatter(s_obs, h_obs, s = 64, alpha = 0.4, color = 'red')
ax.plot(obs_centers, obs_med, linestyle = '--', linewidth = 6, color = 'red', label = 'Behroozi et al.')

ax.legend()
fig.savefig('/cosma5/data/durham/dc-murr1/mass_plot.png')