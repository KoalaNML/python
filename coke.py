amount = 50
change = 0
print("Amount Due:",amount)
while amount > 0:
    print("Amount Due:",amount)
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount -= coin
        if amount < 0:
            change -= amount
            break

print("Change Owed:",change)