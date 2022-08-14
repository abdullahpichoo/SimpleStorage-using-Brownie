from brownie import SimpleStorage, accounts, network
import random, os

# 3 steps for testing: .Arrange .Act .Assert
def get_acc():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(os.getenv("priv_key"))


def get_contract():
    return SimpleStorage.deploy({"from": get_acc()})


def test_num():
    acc = get_acc()
    contract = get_contract()
    size = 10
    expected_arr = []
    for i in range(size):
        n = random.randint(0, 100)
        expected_arr.append(n)
        trx = contract.addNum(n, {"from": acc})
        trx.wait(1)
    assert expected_arr == contract.getNums()


def test_peeps():
    acc = get_acc()
    contract = get_contract()
    expected_peeps = []
    coins = ["BTC", "ETH", "SOL", "AVAX", "ONE", "LINK", "DOT"]
    for i in range(len(coins)):
        rand_balance = random.randint(0, 50)
        rand_coin = coins[random.randint(0, len(coins) - 1)]
        rand_name = chr(ord("a") + random.randint(0, 10))
        expected_peeps.append((rand_balance, rand_coin, rand_name))
        trx = contract.addPerson(rand_name, rand_balance, rand_coin, {"from": acc})
        trx.wait(1)
    assert expected_peeps == contract.getPersons()
