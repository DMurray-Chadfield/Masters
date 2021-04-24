from velociraptor import load
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy

cat = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

sfr = cat.star_formation_rate.sfr_gas
struc = cat.structure_type.structuretype
m30 = cat.masses.m_star_30kpc
age = cat.stellar_age.tage_star


where1 = numpy.where(struc == 10)[0]

sfr = sfr[where1]
m30 = m30[where1]
age = age[where1]

where2 = numpy.where(sfr == 0)[0]

m30 = m30[where2]
age = age[where2]

where3 = numpy.where(m30 > 0)

m30 = m30[where3]
age = age[where3]

fig, ax = pyplot.subplots()
ax.scatter(age, m30)
ax.loglog()
fig.savefig('/cosma5/data/durham/dc-murr1/non_star_forming_halos.png')
