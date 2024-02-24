class BankSystem:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register(self):
        email = input("Enter your email: ")
        if email in self.users:
            print("Email already registered. Please log in.")
            return

        password = input("Enter your password: ")
        self.users[email] = {'password': password, 'balance': 0}
        print("Registration successful!")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.users and self.users[email]['password'] == password:
            self.current_user = email
            print(f"Welcome, {email}!")
        else:
            print("Invalid email or password. Please try again.")

    def perform_transaction(self, transaction_type):
        if not self.current_user:
            print("You need to log in first.")
            return

        amount = float(input(f"Enter the {transaction_type} amount: "))

        if transaction_type == 'deposit':
            if amount > 0:
                self.users[self.current_user]['balance'] += amount
                print(f"{transaction_type.capitalize()} successful. New balance: {self.users[self.current_user]['balance']}")
            else:
                print("Invalid amount. Please enter a positive number.")
        elif transaction_type == 'withdraw':
            if 0 < amount <= self.users[self.current_user]['balance']:
                self.users[self.current_user]['balance'] -= amount
                print(f"{transaction_type.capitalize()} successful. New balance: {self.users[self.current_user]['balance']}")
            elif amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                print("Insufficient funds. Withdrawal failed.")

    def check_balance(self):
        if not self.current_user:
            print("You need to log in first.")
            return

        balance = self.users[self.current_user]['balance']
        print(f"Your current balance: {balance}")

    def logout(self):
        if self.current_user:
            print(f"Goodbye, {self.current_user}!")
            self.current_user = None
        else:
            print("You are not logged in.")

if __name__ == "__main__":
    bank = BankSystem()

    while True:
        print("\nBank System Menu:\n"
              "1. Register\n"
              "2. Log In\n"
              "3. Deposit\n"
              "4. Withdraw\n"
              "5. Check Balance\n"
              "6. Log Out\n"
              "7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bank.register()
        elif choice == '2':
            bank.login()
        elif choice == '3':
            bank.perform_transaction('deposit')
        elif choice == '4':
            bank.perform_transaction('withdraw')
        elif choice == '5':
            bank.check_balance()
        elif choice == '6':
            bank.logout()
        elif choice == '7':
            print("Exiting the Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")