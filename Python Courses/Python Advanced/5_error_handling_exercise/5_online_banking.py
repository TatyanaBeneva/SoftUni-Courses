class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = input().split(", ")
balance = float(balance)
age = int(age)
command = input()

while command != "End":
    action, operation = command.split()

    if action == "Send":
        _, money, pin = operation.split("#")
        money = float(money)

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        elif pin != pin_code:
            raise PINCodeError("Invalid PIN code")
        elif age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif action == "Receive":
        _, money = operation.split("#")
        money = float(money)

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        money_to_add = money / 2
        balance += money_to_add
        print(f"{money_to_add:.2f} money went straight into the bank account")

    command = input()