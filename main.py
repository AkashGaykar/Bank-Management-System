from bank import *
from registration import *
status = False
print("Welcome to SBI Bank")
while True:
    try:
        register = int(input("1. Signup \n2.SignIn  :"))
        if register ==1 or register == 2 :
            if register == 1 :
                SignUp()
            if register ==2 :
                user = SignIn()
                status = True
                break
        else:
            print("Enter Valid Input")
        
        
    except ValueError:
        print("Invalid Input")
        
account_number = queryExecution(f"SELECT account_number FROM sbi_bank WHERE username = '{user}';")

while status:
    print(f"Welcome {user}")
    print(f"Choose Your Banking Service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Exit\n "
                             "Enter Your Choice :"
                             ))
        
        if facility >=1 and facility<=4:
            if facility==1:
                bank_obj = Bank(user,account_number[0][0])
                bank_obj.balance_enquiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter amount to Deposite"))
                        bank_obj = Bank(user,account_number[0][0])
                        bank_obj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input")
                        continue
            
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("enter amount to be withdraw :"))
                        bank_obj = Bank(user,account_number[0][0])
                        bank_obj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("enter valid input")
                        continue
        
            elif facility ==4 :
                print("Thanks for Using banking Services")
                status =  False
        
        else:
            print("Please Enter Valid Input from options")
            continue
                

    
    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue