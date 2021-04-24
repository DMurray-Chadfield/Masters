from velociraptor import load

data = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_0037/halo_0037.properties')

print(data.masses.mvir[0], data.masses.mass_200crit[0])