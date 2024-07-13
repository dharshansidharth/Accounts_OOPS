class BalanceException(Exception):
    pass

class bankAccounts:
    def __init__(self , name : str , balance : float) -> None:
        self.name = name
        self.balance = balance
        print(f"\nAccount created with name '{name}'\nBalance = Rs.{balance:.2f}\n")

    def get_name(self) -> str:
        return self.name

    def get_balance(self) -> float:
        print(f"\nAccount name: '{self.name}'\nBalance = {self.balance:.2f}\n")
        return self.balance

    def deposit(self , amount) -> None:
        self.balance += amount
        print("\nDeposit Successful!\n")
        self.get_balance()

    def viableTransaction(self , amount) -> None:
        if self.balance >= amount:
           return
        else:
            raise BalanceException(f'\nNo enough money to withdraw!\nBalance = {self.balance:.2f}')
    def withdraw(self , amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print('\nWithdraw successful!\n')
            self.get_balance()
            return amount
        except BalanceException as error:
            print("\nWithdraw Interrupt!\n")
            print(f'{error}')

    def transfer(self , amount , account):
        try :
            print('')
            print(''.center(20 , "*"))
            self.viableTransaction(amount)
            temp = self.withdraw(amount)
            account.deposit(temp)
            print('Transfer Successful!')
            print('')
            print(''.center(20 , "*"))
        except BalanceException as error:
            print('Transfer Interrupt!')
            print(f"{error}")

class interestAccount(bankAccounts):
    def deposit(self , amount):
        self.balance += amount * 0.05 + amount
        print('\nDeposit Successful\n')
        self.get_balance()

class savingsAccount(interestAccount):
    def __init__(self , amount , account):
        super().__init__(amount , account)
        self.fee = 5

    def withdraw(self , amount) :
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print('\nWithdraw successful!\n')
            self.get_balance()
            return amount
        except BalanceException as error:
            print("\nWithdraw Interrupt!\n")
            print(f'{error}')


        
        

    