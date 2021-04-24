from swiftsimio import load
data = load('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_0037.hdf5')
print(dir(data.gas))
print(dir(data.units))