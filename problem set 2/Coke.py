acceptable_coins = [10, 25, 50]

amount_due = 50

while amount_due > 0:

    print(f"amount_due: {amount_due}")

    coin = int(input("Inster Coin: "))

    if coin in acceptable_coins:
            amount_due -= coin

print(f"change owe = {abs(amount_due)}")


