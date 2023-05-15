class BalanceException(Exception):
    pass

def checkbalance(withdraw):
    money=10000
    withdraw=90000
    balance=money-withdraw
    if(balance<=2000):
        raise BalanceException('Insufficient Balance !!!')
    print(balance)

try:
    checkbalance()
except BalanceException as b:
    print(b)