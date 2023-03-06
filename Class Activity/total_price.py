def total_price():
    try:
        total_price = 0
        amount = int(input('Enter the amount: '))
        price = int(input('Enter the price: '))
        total_price = amount * price
        if (amount < 0 or price < 0):
            raise ValueError

    except ValueError:
        total_price = 0
        print("Invalid Input")

    finally:
        print("Your total price is", total_price)

total_price()
