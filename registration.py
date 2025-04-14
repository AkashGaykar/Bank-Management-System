from dbaccess import *
from bank import Bank
import random
from customer import Customer


def SignUp():
    username = input("Create Username :")
    temp = queryExecution(f"SELECT username FROM sbi_bank WHERE username ='{username}';")
    if temp:
        print("Username Already Exists")
        SignUp()
    else:
        print("Username is Accepted.")
        password = input("Enter Your Password :")
        name = input("Enter Your Name : ")
        age = input("Enter Your Age : ")
        city =input("Enter Your City: ")
        
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = queryExecution(f"SELECT account_number FROM sbi_bank WHERE account_number = '{account_number}';")
            if temp :
                continue
            else:
                print("Your Account Number is :",account_number)
                break
    
    customer_obj = Customer(username,password,name,age,city,account_number)
    customer_obj.createUser()
    bank_obj = Bank(username,password)
    bank_obj.create_transaction_table()
    

def SignIn():
    username = input("Enter Username :")
    temp = queryExecution(f"SELECT username from sbi_bank WHERE username= '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()}\n Please Enter Your Password :")
            temp = queryExecution(f"SELECT password FROM sbi_bank WHERE username = '{username}';")
            if temp[0][0] == password:
                print("Sign In Successfully")
                print("Your Password is :",password)
                return username
            else:
                print("Incorrect Password. Try Again")
                continue
    else:
        print("Enter Correct Username")
        SignIn()