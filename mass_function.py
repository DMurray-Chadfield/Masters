from velociraptor import load
import numpy

data = load("/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties")

masses_200crit = data.masses.mass_200crit
masses_200crit.convert_to_units("kg")
struc = data.structure_type.structuretype

from velociraptor.tools import create_mass_function
from velociraptor.tools.labels import get_full_label, get_mass_function_label
from velociraptor import tools
from unyt import Mpc
import unyt
import matplotlib
from matplotlib import pyplot
matplotlib.use('Agg')
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)

pyplot.rcParams.update({'font.size':40})

# Convert to stellar masses because that 'makes sense'
masses_200crit.convert_to_units("msun")
mask = numpy.where(struc == 10)[0]
masses_200crit = masses_200crit[mask]
mask2 = numpy.where(masses_200crit > 0)[0]
masses_200crit = masses_200crit[mask2]

box_volume = (25 * Mpc)**3

# Set the edges of our halo masses,
lowest_halo_mass = numpy.amin(masses_200crit)
highest_halo_mass = numpy.amax(masses_200crit)

bin_centers, mass_function, error = tools.create_mass_function(
   masses_200crit, lowest_halo_mass, highest_halo_mass, box_volume
)

mass_label = get_full_label(masses_200crit)
mf_label = r'$dn(M_{200crit})/dM_{200crit}[Mpc^{-3}]$'

obs = numpy.loadtxt('/cosma5/data/durham/dc-murr1/hmf_data.txt')
m_obs = obs[:,0]
tinker = obs[:,1]
bocquet = obs[:,2]

fig, ax1 = pyplot.subplots(figsize = (20,20))
ax1.errorbar(bin_centers, mass_function, error, linewidth = 5, label = 'EAGLE')
ax1.plot(m_obs, tinker, marker = '', linewidth = 5, label = 'Tinker et al.')
ax1.plot(m_obs, bocquet, marker = '', linewidth = 5, label = 'Bocquet et al.')
ax1.set_xlabel(mass_label)
ax1.set_ylabel(mf_label)
ax1.loglog()
ax1.legend()

ax2 = pyplot.axes([0,0,1,1])
ip = InsetPosition(ax1, [0.1,0.1,0.4,0.4])
ax2.set_axes_locator(ip)
mark_inset(ax1, ax2, loc1=2, loc2=4, fc="none", ec='0.5')
ax2.errorbar(bin_centers, mass_function, error, linewidth = 5)
ax2.plot(m_obs, tinker, marker = '', linewidth = 5)
ax2.plot(m_obs, bocquet, marker = '', linewidth = 5)
ax2.set_ylim(10**(-2), 1)
ax2.set_xlim(10**9, 10**11)
ax2.loglog()
ax2.axes.xaxis.set_visible(False)
ax2.axes.yaxis.set_visible(False)
fig.savefig('/cosma5/data/durham/dc-murr1/mass_function.png')

