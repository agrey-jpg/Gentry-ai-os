from agency_swarm import Agency

from chief_of_staff import chief_of_staff
from miner import miner


agency = Agency(
    chief_of_staff,
    communication_flows=[
        (chief_of_staff, miner),
    ],
)


if __name__ == "__main__":
    agency.run_demo()
