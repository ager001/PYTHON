import logging

# Setup logging
logging.basicConfig(
    filename="atm_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class InsufficientFundsError(Exception):
    pass
# ATM Class
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than 0")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")

        self.balance -= amount
        return self.balance


# ---------------- MAIN PROGRAM ----------------

atm = ATM(balance=1000)

try:
    amount = int(input("Enter withdrawal amount: "))

    new_balance = atm.withdraw(amount)
    print(f"Withdrawal successful. New balance: {new_balance}")

except ValueError as e:
    logging.error(f"Invalid input error: {e}")

except InsufficientFundsError as e:
    logging.error(f"ATM error: {e}")

except Exception as e:
    logging.error(f"Unexpected error: {e}")

finally:
    print("Thank you for using our ATM")