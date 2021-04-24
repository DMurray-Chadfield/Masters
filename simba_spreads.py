from transfer.spreadmetric import SpreadMetricCalculator
from transfer.frontends.simbaahf import SIMBASnapshotData
from transfer.holder import SimulationData
import pickle

initial_filename = "/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_000.hdf5"
final_filename = "/cosma6/data/dp004/dc-borr1/simba-test-data/snap_m50n512_151.hdf5"

initial_halo_filename = None
final_halo_filename = ("/cosma6/data/dp004/dc-borr1/simba-test-data/snap151Rpep..z0.000.AHF_halos")

initial = SIMBASnapshotData(initial_filename, initial_halo_filename)

truncate_ids = {
0: initial.gas.particle_ids.max() + 1,
1: None,
4: initial.gas.particle_ids.max() + 1,
}

final = SIMBASnapshotData(final_filename, final_halo_filename, truncate_ids=truncate_ids)
cross = SimulationData(initial_snapshot=initial, final_snapshot=final)

for particle_type in ["dark_matter", "stars", "gas"]:
    x = {
        n: getattr(getattr(cross, f"{particle_type}_transfer"), n)
        for n in [
            "in_halo",
            "in_halo_from_own_lr",
            "in_halo_from_other_lr",
            "in_halo_from_outside_lr",
            "in_lr",
            "in_other_halo_from_lr",
            "outside_haloes",
        ]
    }   
with open(f"{particle_type}.pickle", "wb") as handle:
    pickle.dump(x, handle)

with open(f"haloes.pickle", "wb") as handle:
    pickle.dump(
    {
        "halo_coordinates": cross.final_snapshot.halo_coordinates,
        "halo_radii": cross.final_snapshot.halo_radii,
    },
    handle,
)

spread_metric = SpreadMetricCalculator(simulation=cross)
spread_metric.find_neighbour_distances()


spread_metric.dark_matter_spread.write_hdf5("/cosma5/data/durham/dc-murr1/dark_matter_spread.hdf5")
spread_metric.gas_spread.write_hdf5("/cosma5/data/durham/dc-murr1/gas_spread.hdf5")
spread_metric.star_spread.write_hdf5("/cosma5/data/durham/dc-murr1/star_spread.hdf5")
