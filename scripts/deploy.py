from brownie import accounts, SimpleStorage, network
import os, random


def get_acc():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(os.getenv("priv_key"))


def get_contract():
    return SimpleStorage.deploy({"from": get_acc()})


def deploy_simple_storage():
    acc = get_acc()
    contract = get_contract()
    coins = ["BTC", "ETH", "SOL", "AVAX", "ONE", "LINK", "DOT"]
    for i in range(len(coins)):
        rand_balance = random.randint(0, 50)
        rand_coin = coins[random.randint(0, len(coins) - 1)]
        rand_name = chr(ord("a") + random.randint(0, 10))
        trx = contract.addPerson(rand_name, rand_balance, rand_coin, {"from": acc})
        trx.wait(1)
    print(contract.getPersons())


def main():
    deploy_simple_storage()
