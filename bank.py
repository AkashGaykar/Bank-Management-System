from dbaccess import *
import datetime

class Bank:
    def __init__(self,username,account_number):
        self._username = username
        self._account_number = account_number
    
    def create_transaction_table(self):
        queryExecution(f"""
                       CREATE TABLE IF NOT EXISTS {self._username}_transaction(
                           timedate VARCHAR(60),
                           account_number INTEGER,
                           remarks VARCHAR(30),
                           amount INTEGER,
                           balance INTEGER
                       )
                       """)
        
    def balance_enquiry(self):
        temp = queryExecution("SELECT balance From sbi_bank WHERE username =%s;",(self._username,))
        balance = temp[0][0] if temp else 0
        print(f"{self._username}'s Balance is Rs.{balance:,.2f}")
        
    def deposit(self,amount):
        temp = queryExecution("SELECT balance FROM sbi_bank WHERE username =%s;",(self._username,))
        new_bal = amount + temp[0][0]
        queryExecution("UPDATE sbi_bank SET balance=%s WHERE username =%s;",(new_bal,self._username))
        self.balance_enquiry()
        queryExecution(f"""
            INSERT INTO {self._username}_transaction 
            VALUES ('{datetime.datetime.now()}',{self._account_number}, 'Amount Deposit', {amount},{new_bal});
        """)
        masked_account_number = '*' * (len(str(self._account_number)) - 4) + str(self._account_number)[-4:]
        print(f"Dear User, A/C {masked_account_number} credited by Rs.{amount} on {datetime.date.today()}")        
        
    def withdraw(self,amount):
        temp = queryExecution(f"SELECT balance FROM sbi_bank WHERE username =%s;",(self._username,))
        if amount > temp[0][0]:
            print("Insufficirnt Balance")
        else:
            new_bal = temp[0][0] - amount
            queryExecution("UPDATE sbi_bank SET balance = %s WHERE username=%s",(new_bal,self._username) )
            self.balance_enquiry()
            queryExecution(f"""
                           INSERT INTO {self._username}_transaction
                           VALUES ('{datetime.datetime.now()}','{self._account_number}','Debited','{amount}','{new_bal}')
                           """)
            print(f"Dear User , your A/C {self._account_number} debited by Rs.{amount} on {datetime.date.today()}")
