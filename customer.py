from dbaccess import *

class Customer:
    def __init__(self,username,password,name,age,city,account_number):
        self._username =username
        self._password = password
        self._name = name
        self._age = age
        self._city =city
        self._account_number = account_number
        
    
    def createUser(self):
        queryExecution(f"INSERT INTO sbi_bank Values('{self._username}','{self._password}','{self._name}','{self._age}','{self._city}', 0 ,'{self._account_number}', True )")
        mydb.commit()