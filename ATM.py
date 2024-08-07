class ATM:
    def __init__(self):
        self.balance = 0
    
    def display_menu(self):
        print("Welcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your new balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: $"))
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Your new balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")

# Create an ATM instance and run it
atm = ATM()
atm.run()
