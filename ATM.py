class Bank:

    def __init__(self):
        self.acbal = 10000
        self.transactions = 0

    def notes(self, amt):
        n500 = amt // 500
        amt %= 500

        n200 = amt // 200
        amt %= 200

        n100 = amt // 100

        print("Notes given:")
        print("500 :", n500)
        print("200 :", n200)
        print("100 :", n100)

    def deposit(self):
        amt = int(input("Enter deposit amount: "))

        if amt % 100 != 0:
            print("Enter multiples of 100 only")
            return

        self.acbal += amt
        self.transactions += 1

        print("Deposit successful")
        self.notes(amt)   # ✅ added
        print("Available balance:", self.acbal)

    def withdraw(self):
        amt = int(input("Enter withdraw amount: "))

        if amt % 100 != 0:
            print("Enter multiples of 100 only")
            return

        if amt > 20000:
            print("Withdraw limit is 20k only")
            return

        if amt > self.acbal:
            print("Insufficient balance")
            return

        self.acbal -= amt
        self.transactions += 1

        print("Please collect your cash")
        self.notes(amt)
        print("Available balance:", self.acbal)

    def balance(self):
        print("Available balance:", self.acbal)

    def viewOptions(self):

        while True:

            if self.transactions >= 3:
                print("\nDaily transaction limit reached (3)")
                break

            print("\n------ ATM MENU ------")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance Enquiry")
            print("0. Exit")

            option = int(input("Choose your option: "))

            if option == 1:
                self.deposit()

            elif option == 2:
                self.withdraw()

            elif option == 3:
                self.balance()

            elif option == 0:
                print("Thank you, visit again")
                
                break

            else:
                print("Invalid option")

            cont = input("\nDo you want to continue? (y/n): ")

            if cont.lower() != 'y':
                break


obj = Bank()
obj.viewOptions()
