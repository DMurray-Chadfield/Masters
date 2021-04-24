from velociraptor import load
from swiftsimio import load as load_snap
from unyt import unyt_array
from scipy.spatial import cKDTree
import numpy

catalogue = load('/cosma6/data/dp004/dc-borr1/swift-test-data/halo_2730/halo_2730.properties')
snap = load_snap('/cosma6/data/dp004/dc-borr1/swift-test-data/eagle_2730.hdf5')

centrals = catalogue.structure_type.structuretype == 10
dm_data = getattr(snap, 'dark_matter', None)
boxsize = snap.metadata.boxsize
tree = cKDTree(dm_data.coordinates.value, boxsize=boxsize.value)

halo_coordinates = (
            unyt_array(
                [
                    getattr(catalogue.positions, f"{x}cmbp")[centrals]
                    for x in ["x", "y", "z"]
                ]
            ).T
            / catalogue.units.a
        )

halo_radii = catalogue.radii.r_200mean[centrals] / catalogue.units.a

block_size = 1024
number_of_haloes = halo_radii.size
number_of_blocks = 1 + number_of_haloes // block_size


starting_index = 1*1024
ending_index = 2*1024


particle_indicies = tree.query_ball_point(x=5, r=4, n_jobs=-1)
