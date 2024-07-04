import time
import sys
import cardHolder

def Start_ATM():
    try:
        class ATM(): 
            def __init__(self, balance=0):
                self.balance = balance

            def Check_balance(self):
                print(f"\nYour current balance is {self.balance}Ghc")

            def Deposit(self):
                much=int(input("Enter the amount to deposit: "))
                time.sleep(1)
                num=int(input("Enter your Number "))
                time.sleep(2)
                self.balance+=much
                print("\n=====================")
                print(f"\nDeposit successful.")
                print(f"Your balance is ${self.balance}.")
                print("Thank you for using MK ATM.")
                print("=====================")

            def Withdrawn(self):
                much=int(input("How much do you want to Withdraw? "))
                if much>self.balance:
                    print("Insuffienct balance")
                time.sleep(1)
                pin=int(input("Enter your pin: "))
                print("Loading...")
                self.balance-=much
                time.sleep(2)
                print("\n=====================")
                print("Withdrawal successfully.")
                print(f"Your Balance left is {self.balance}Ghc.")
                print("Thank you for using MK ATM.")
                print("=====================")


            def Main(self):
                while True:
                    print("\n================")
                    print("Select from the Menu")
                    print("1 : Deposit")
                    print("2 : Withdrawal")
                    print("3 : Check Balance")
                    print("4 : Accounts")
                    print("5 : Exit")
                    select=int(input(">"))
                    if(select==1):
                        self.Deposit()
                    elif(select==2):
                        self.Withdrawn()
                    elif(select==3):
                        self.Check_balance()
                    elif(select==4):
                        self.Accounts()
                    elif(select==5):
                        print("\nThanks For using MK ATM.\nHave a nice day.")
                        sys.exit()
                    else:
                        print("\nInput required. Try again")
                        sys.exit()
            
        atm=ATM(balance=1000)
        atm.Main()
    except Exception:
        print("\nInvalid Input.")
        sys.exit()

def login(user="user",passw=0000):
    usernames=cardHolder.usersholder.keys()
    userPins=cardHolder.usersholder.values()
    while True:
        try:
            print("=======================")
            print("🏧 Welcome To MK ATM 🏧".upper())
            print("\nLet's Login To your account!")
            userinput=str(input("Enter cardHolder name: ")).lower()
            passinput=int(input("Enter your password: "))

            if(userinput in usernames or userinput==usernames or userinput=="user"):
                if(passinput in userPins or passinput==userPins or passinput==0000):
                    print(f"👋 Hello {userinput}!")
                    Start_ATM()
                else:
                    print("\nInvalid Password.")
            else:
                print("\nUsername not found.\n")
                continue
        except ValueError:
            print("\nLogin Failed. try again")
        sys.exit()

login(user="user",passw=0000)



    