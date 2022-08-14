from brownie import SimpleStorage, accounts, network

# SimpleStorage is actually an array of addresses of contract deployments
# every index contains a deployed contract and all of its state changes are saved in it


def read_contract():
    contract = SimpleStorage[-1]
    # -1 is used to get the most recent contract deployment
    print(contract.getPersons())


def main():
    read_contract()
