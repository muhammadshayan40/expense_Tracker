from datetime import datetime

#File name where our data stored
FILE_NAME="expenses.txt"

def add_Expenses():
    print("Add Expenses")
    amount=input("Enter amount (PKR):")
    category=input("Enter category (e.g., Food, Travel, Bills):")
    date=input("Enter date (YYYY-MM-DD):")

#our expenses save here    
    with open(FILE_NAME,"a") as f:
        f.write(f"{amount},{category},{date}\n")
        print("Expense added successfully!")
#add_Expenses()   
#---------------------------------------------------------------

def view_Expenses():
    print("\n All Recorded Expenses:")
    
    try:
        with open(FILE_NAME, "r") as f:
            lines=f.readlines()
            if not lines:        # if "lines" is an empty list[],so "not lines" is True
                 print("No expenses found.")
                 return
            
            for line in lines:
                amount, category, date = line.strip().split(",")
                print(f" {amount} PKR |  {category} |  {date}")
                
    #this line is optional, if we not write this we got error bcz of try keyword           
    except FileNotFoundError:
        print("No expenses recorded yet.")   
#view_Expenses()          
 #---------------------------------------------------------------       
              
def search_by_Date():
    print("\nSearch expenses by date")
    search_Date=input("Enter date (YYYY-MM-DD):")
    found= False
    
    try:
        with open(FILE_NAME, "r") as f:
           for line in f:
               amount, category, date = line.strip().split(",")
               if (date == search_Date):
                   print(f"{amount}  |  {category}")
                   found= True
                   
        if not found:
            print("No expenses found for this date.")  
    #optional        
    except FileNotFoundError:
        print("No data found in file")      
search_by_Date ()
#------------------------------------------------------------------------               
                   
    
                        
            
    

    
    