from velociraptor import load
import numpy 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
pyplot.rcParams.update({'font.size':40})
from matplotlib.colors import LogNorm
from velociraptor.tools.lines import binned_median_line as bml
import unyt
from velociraptor.tools.labels import get_full_label

cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')
struc = cat.structure_type.structuretype
where = numpy.where(struc == 10)[0]
m30 = cat.masses.m_star_30kpc
m30.convert_to_units('msun')
sfr = cat.star_formation_rate.sfr_gas
sfr.convert_to_units(unyt.msun / unyt.yr)
m30 = m30[where]
sfr = sfr[where]

where2 = numpy.where(m30 >= 0)[0]
m30 = m30[where2]
sfr = sfr[where2]

non_zero_sfr = numpy.delete(sfr, numpy.where(sfr == 0)[0])
non_zero_m30 = numpy.delete(m30, numpy.where(sfr == 0)[0])
non_zero_sfr = numpy.delete(non_zero_sfr, numpy.where(non_zero_m30 == 0)[0])
non_zero_m30 = numpy.delete(non_zero_m30, numpy.where(non_zero_m30 == 0)[0])

low_sfr = numpy.amin(non_zero_sfr)
low_m30 = numpy.amin(non_zero_m30)
for loc in numpy.where(sfr == 0)[0]:
    sfr[loc] = low_sfr / 2
for loc in numpy.where(m30 == 0)[0]:
    m30[loc] = low_m30 / 2
print(numpy.amin(sfr), numpy.amin(m30), numpy.amin(non_zero_sfr), numpy.amin(non_zero_m30))
fig, ax = pyplot.subplots(figsize = (20,20))
ax.tick_params(length = 10, width = 2, direction = 'in')
bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.amin(non_zero_m30)), numpy.log10(numpy.amax(non_zero_m30)), 20), units = m30.units)
centers, med, err = bml(non_zero_m30, non_zero_sfr, x_bins = bins)
ax.scatter(m30, sfr, marker = 'o', s = 20)
ax.plot(centers, med, linestyle = '--', linewidth = 5, color = 'black')
ax.loglog()
ax.set_ylabel(get_full_label(sfr))
ax.set_xlabel(get_full_label(m30))
fig.savefig('/cosma5/data/durham/dc-murr1/sfr_stellar_mass.png')