import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password = "akash",
    database="bank"
)

cursor = mydb.cursor()

def queryExecution(query,params=None):
    if params:
        cursor.execute(query,params)
    else:
        cursor.execute(query)
        
    if query.strip().upper().startswith("SELECT"):
        result = cursor.fetchall()
        return result
    else:
        mydb.commit()
        return None

def createCustomerTable():
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS sbi_bank (
                       username VARCHAR(50) NOT NULL,
                       password VARCHAR(50) NOT NULL,
                       name VARCHAR(20) NOT NULL,
                       age INTEGER NOT NULL,
                       city VARCHAR(30) NOT NULL,
                       balance INTEGER NOT NULL,
                       account_number INTEGER PRIMARY KEY NOT NULL,
                       status BOOLEAN NOT NULL)
                   ''')
    
    mydb.commit()
    
if __name__ == "__main__":
    createCustomerTable()