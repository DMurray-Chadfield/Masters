from velociraptor import load
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy
from velociraptor.tools.labels import get_full_label
import unyt
from velociraptor.observations import load_observation

pyplot.rcParams.update({'font.size':40})

data = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties', disregard_units = True)
obs = numpy.loadtxt('/cosma5/data/durham/dc-murr1/Zahid2014.txt')



mass = data.masses.m_star_30kpc
x = data.metallicity.zmet_gas
mass.convert_to_units('msun')

x_wh = numpy.where(x != 0)[0]
mass = mass[x_wh]
x = x[x_wh]
m_wh = numpy.where(mass != 0)[0]
x = x[m_wh]
mass = mass[m_wh]

xlabel = get_full_label(mass)
ylabel = get_full_label(x)

obs = numpy.loadtxt('/cosma5/data/durham/dc-murr1/Zahid2014.txt')
m_obs = obs[:,0]
x_obs = obs[:,1]
x_obs = 10**(x_obs - 12)


from velociraptor.tools.lines import binned_median_line as bml

mass_bins = numpy.logspace(numpy.log10(numpy.min(mass).value), numpy.log10(numpy.max(mass).value), 20)
mass_bins = unyt.unyt_array(mass_bins, units = mass.units)
centers, med, err = bml(mass, x, mass_bins, minimum_in_bin = 1)

obs_bins = numpy.logspace(numpy.log10(numpy.min(m_obs)), numpy.log10(numpy.max(m_obs)), 20)
obs_bins = unyt.unyt_array(obs_bins, units = mass.units)
m_obs = unyt.unyt_array(m_obs, units = mass.units)
x_obs = unyt.unyt_array(x_obs, units = x.units)
obs_centers, obs_med, obs_err = bml(m_obs, x_obs, obs_bins, minimum_in_bin = 1)

fig, ax = pyplot.subplots(figsize = (20,20))
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
ax.scatter(mass, x, s = 64, alpha = 0.4, color = 'blue')
ax.plot(centers, med, linestyle = '--', linewidth = 6, color = 'blue', label = 'EAGLE')
ax.loglog()
ax.scatter(m_obs, x_obs, s = 64, alpha = 0.4, color = 'red')
ax.plot(obs_centers, obs_med, linestyle = '--', linewidth = 6, color = 'red', label = 'Zahid et al.')
ax.legend()
fig.savefig('/cosma5/data/durham/dc-murr1/mass_X.png')

