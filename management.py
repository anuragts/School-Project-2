import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# Hotel Manangement system in python with mysql database.
password = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=f'{password}',
    database="hotel_management"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE IF NOT EXISTS hotel_management")
# mycursor.execute("USE hotel_management")

# table_name = None
def create_table():
    table_name = input("Enter the table name: ")
    enter_columns = input("Enter the columns: ")
    print("")
    new_table = f"CREATE TABLE hotel_management.{table_name}(id INT AUTO_INCREMENT PRIMARY KEY, {enter_columns} VARCHAR(255))"
    mycursor.execute(new_table)
    print(f"Table {table_name} created successfully")
    response = input("Do you want to add more Columns (Y/N) : ")
    add_columns(response, table_name)

def add_columns(response, table_name):
    response = response.upper()
    if response == "Y":
        enter_columns = input("Enter the column name : ")
        mycursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {enter_columns} VARCHAR(255)")
        print(f"Added {enter_columns} successfully")
        start()
    elif response=="YES" and table_name == None :    
        table_name = input("Enter the table name: ")
        enter_columns = input("Enter the column name : ")
        mycursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {enter_columns} VARCHAR(255)")
        print(f"Added {enter_columns} successfully")
        start() 
    elif response == "N":
        print("Thank you")
    else:
        print("Invalid Input !!")
        add_columns(response, table_name)
    

def start():
    print("""
    What do you want to do?
    1. Create Table
    2. Add Columns
    3. Exit
    """)
    response = input("Enter your choice : ")
    if response == "1":
        create_table()
    elif response == "2":
        add_columns(table_name=None,response="YES")
    elif response == "3":
        print("Thank you")
    else:
        print("Invalid Input !!")
        start()   
start()
        

    


