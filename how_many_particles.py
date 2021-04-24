import numpy

adi_gas = len(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_gas_nearest_halos.txt'))
adi_dm = len(numpy.loadtxt('/cosma5/data/durham/dc-murr1/adi_dm_nearest_halos.txt'))
eagle_gas = len(numpy.loadtxt('/cosma5/data/durham/dc-murr1/gas_nearest_halos.txt'))
eagle_dm = len(numpy.loadtxt('/cosma5/data/durham/dc-murr1/dm_nearest_halos.txt'))
simba_gas = len(numpy.loadtxt('/cosma5/data/durham/dc-murr1/simba_gas_nearest_halos.txt'))
simba_dm = len(numpy.loadtxt('/cosma5/data/durham/dc-murr1/simba_dm_nearest_halos.txt'))


print(adi_gas + adi_dm)
print(eagle_gas + eagle_dm)
print(simba_gas + simba_dm)