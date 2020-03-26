


class Account: 
    def __init__(self): 
        self.balance=0
        self.history = []
        print("Hello!!!")

    def deposit(self): 
        amount = float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        output_one = print("Amount Deposited:", amount)
        self.history.append("Amount Deposited:")
        self.history.append(amount)
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount
            self.history.append("Amount Withdrawn:")
            self.history.append(amount)
            print("Amount Withdrawn", amount)
        else: 
            output_two = print("\n Insufficient balance")
            self.history.append(amount)

    def check_transactions(self): 
        print("Net Available Balance=",self.balance)
        print(self.history)

 a = Account()

while True: 

    user_input = input("What would you like to do(deposit, withdraw, check transactions)?")
        
    if user_input=="deposit":
        a.deposit()
        a.check_transactions()

    elif user_input=="withdraw":
        a.withdraw()
        a.check_transactions()

    elif user_input=="check transactions":
        a.check_transactions()



    

           
  

