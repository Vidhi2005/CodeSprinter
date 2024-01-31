class CryptoBank:
    def _init_(self):
        self.total_amount = 0
        self.loan_amount = 0
        self.loan_interest_rate = 0

    def deposit(self, amount):
        self.total_amount += amount
        print(f"Amount {amount} credited successfully.")
        self.display_balance()

    def withdraw(self, amount):
        if amount <= self.total_amount:
            self.total_amount -= amount
            print(f"Amount {amount} withdrawn successfully.")
            self.display_balance()
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Total Balance: {self.total_amount}")

    def convert_to_cash(self, amount, conversion_rate):
        cash_amount = amount * conversion_rate
        print(f"The liquid cash equivalent of {amount} is {cash_amount}")

    def take_loan(self, amount, duration):
        if amount <= 10000:
            self.loan_interest_rate = 0.05  # 5% interest rate
        else:
            self.loan_interest_rate = 0.02  # 2% interest rate for amounts more than 10000

        total_loan = amount * (1 + self.loan_interest_rate)
        self.loan_amount += total_loan

        print(f"Loan of {amount} taken for {duration} months with {self.loan_interest_rate*100}% interest rate.")
        print(f"Total amount to be repaid: {total_loan}")

    def repay_loan(self, amount):
        if amount <= self.loan_amount:
            interest_paid = amount - (amount / (1 + self.loan_interest_rate))
            self.loan_amount -= amount
            print(f"Loan repayment of {amount} successful.")
            print(f"Interest rate for this loan: {self.loan_interest_rate*100}%")
            print(f"Interest paid: {interest_paid}")
        else:
            print("Invalid repayment amount!")


def main():
    bank = CryptoBank()
    conversion_rate = 5
   
    total_amount = float(input("Enter total amount to start with: "))
    bank.deposit(total_amount)
   
    while True:
        print("\n1. Withdraw")
        print("2. Deposit")
        print("3. Display Balance")
        print("4. Convert to Liquid Cash")
        print("5. Take Loan")
        print("6. Repay Loan")
        print("7. Exit")
       
        choice = input("Enter your choice: ")

        if choice == "1":
            amount_to_withdraw = float(input("Enter amount to withdraw: "))
            bank.withdraw(amount_to_withdraw)
        elif choice == "2":
            amount_to_deposit = float(input("Enter amount to deposit: "))
            bank.deposit(amount_to_deposit)
        elif choice == "3":
            bank.display_balance()
        elif choice == "4":
            amount = float(input("Enter amount to convert: "))
            bank.convert_to_cash(amount, conversion_rate)
        elif choice == "5":
            loan_amount = float(input("Enter loan amount: "))
            loan_duration = int(input("Enter loan duration (in months): "))
            bank.take_loan(loan_amount, loan_duration)
        elif choice == "6":
            repayment_amount = float(input("Enter amount to repay loan: "))
            bank.repay_loan(repayment_amount)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if _name_ == "_main_":
    main()