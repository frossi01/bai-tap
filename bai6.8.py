class Bank:
    Acconunt_type="Savings"
    location="Guntur"
    def __init__(selt, nam, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance=balance
        self.account_type=Bank.Account_type
        self.location=Bank.location

    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        print("------------------------------")
        account_pin=int(input("Please enter your pin number"))
        if(account_pin==123):
            Account(self)
        else:
            print("pin incorrect.please try again")
            error(self)
        return ' '.join([self.nam,self.account_number])
def Error (self):
    account_pin = int (input ("Please enter your pin number "))
    if (account_pin==123):
         Account (self)
    else:
        print ("Pin Incorrect. Please try again")
        Error (self)
    def Account (self):
        print ("our Card Number is:XXXX XXXX XXXX 1337")
        print ("Would you like to deposit/withdraw/Check Balarce?")
        print ("""
1)      Balance
2)      Withdraw
3)      Deposit
4)      Quit
""")
    Option=int (input ("Please enter your choice :"))
    if (option==1):
        Balance (self)
    elif (option==2):
        Withdraw (self)
    elif (option==3) :
        Deposit (self)
    elif (option==4):
        exit ()
def Balance (self) :
    print ("Balance:",self.balance)
    Account (self)
def Withdraw (self) :
    W=int (input ("Please Enter Desired amount: "))
    if(self.balance>0 and self.balance>=w):
        self.balance=self.balance-w
        print ("Your transaction is successfull")
        print ("your Balance:",self.balance)
        print ("")
    else:
        print ("Your transaction is cancelled due to")
        print ("Amount is not sufficient in your account")
    Account(self)
def Deposit(self):
    d=int(input ("Please Enter Desired amourt: "))
    self.balance=self.balarce+d
    print("Your transaction is successfull")
    print("Balance:",self.balance)
    Account(self)
def Exit():
    print ("Exit") 
t1 = Bank('mahesh', 1453210145,5000)
print(t1)
