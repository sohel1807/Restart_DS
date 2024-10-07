class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner      # Public attribute
        self.__balance = balance  # Private attribute (encapsulated)

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} into {self.owner}'s account.")
        else:
            print("Invalid deposit amount!")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account.")
        else:
            print("Insufficient balance or invalid amount.")

    # Public method to check the balance
    def check_balance(self):
        return f"{self.owner}'s account balance: {self.__balance}"

# Example usage
account = BankAccount("Alice", 1000)

# Accessing public methods
account.deposit(500)
account.withdraw(200)

# Checking the balance
print(account.check_balance())

# Trying to access the private attribute directly (This will raise an AttributeError)
# print(account.__balance)  # Uncommenting this will cause an error

# Correct way to access balance via the public method
print(account.check_balance())
