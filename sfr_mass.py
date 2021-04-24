from velociraptor import load
from velociraptor.particles import load_groups
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy
from velociraptor.tools.labels import get_full_label
import unyt

pyplot.rcParams.update({'font.size':40})

data = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties', disregard_units = True)

structure = data.structure_type.structuretype

stellar_form = data.apertures.sfr_gas_30_kpc
stellar_form.convert_to_units('msun/yr')
mass = data.masses.m_star_30kpc
mass.convert_to_units('msun')

structure = numpy.delete(structure, numpy.where(mass <= 0)[0], 0)
stellar_form = numpy.delete(stellar_form, numpy.where(mass <= 0)[0], 0)
mass = numpy.delete(mass, numpy.where(mass <= 0)[0], 0)
structure = numpy.delete(structure, numpy.where(stellar_form <= 0)[0], 0)
mass = numpy.delete(mass, numpy.where(stellar_form <= 0)[0], 0)
stellar_form = numpy.delete(stellar_form, numpy.where(stellar_form <= 0)[0], 0)
mass = numpy.delete(mass, numpy.where(structure != 10)[0], 0)
stellar_form = numpy.delete(stellar_form, numpy.where(structure != 10)[0], 0)
structure = numpy.delete(structure, numpy.where(structure != 10)[0], 0)

from velociraptor.tools.lines import binned_median_line as bml

mass_bins = numpy.logspace(numpy.log10(numpy.min(mass)),numpy.log10(numpy.max(mass)), 20)
mass_bins = unyt.unyt_array(mass_bins, units = mass.units)
centers, med, err = bml(mass, stellar_form, mass_bins, minimum_in_bin = 1)

ylabel = get_full_label(stellar_form)
xlabel = get_full_label(mass)
fig, ax = pyplot.subplots(figsize = (20,20))
ax.scatter(mass, stellar_form, marker = 'o', alpha = 0.4, s = 64, color = 'blue')
ax.plot(centers, med, color = 'blue', linestyle = '--', linewidth = 7, label = 'EAGLE')
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)

obs = numpy.loadtxt('/cosma5/data/durham/dc-murr1/Davies2016.txt', delimiter = ',')
m_obs = obs[:,0]
sfr_obs = obs[:,1]

obs_bins = numpy.logspace(numpy.log10(numpy.min(m_obs)), numpy.log10(numpy.max(m_obs)), 20)
m_obs = unyt.unyt_array(m_obs, units = mass.units)
sfr_obs = unyt.unyt_array(sfr_obs, units = stellar_form.units)
obs_bins = unyt.unyt_array(obs_bins, units = mass.units)
obs_centers, obs_med, obs_err = bml(m_obs, sfr_obs, obs_bins, minimum_in_bin = 1)

ax.scatter(m_obs, sfr_obs, marker = 'o', alpha = 0.4, s = 64, color = 'red')
ax.plot(obs_centers, obs_med, color = 'red', linestyle = '--', linewidth = 7, label = 'Davies et al.')

ax.legend()

fig.savefig('/cosma5/data/durham/dc-murr1/sfr_mass.png')
