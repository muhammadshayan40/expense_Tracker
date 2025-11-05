from datetime import datetime
from collections import defaultdict


#File name where our data stored
FILE_NAME="expenses.txt"

#-------------------------------------------------------
#                 ADD EXPENSES
def add_Expenses():
    print("Add Expenses")
    amount=input("Enter amount (PKR):")
    category=input("Enter category (e.g., Food, Travel, Bills):")
    date=input("Enter date (YYYY-MM-DD):")

#our expenses save here    
    with open(FILE_NAME,"a") as f:
        f.write(f"{amount},{category},{date}\n")
        print("Expense added successfully!")
   
#---------------------------------------------------------------
#                   VIEW EXPENSES
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
        
 #---------------------------------------------------------------       
#                   SEARCH BY DATE              
def search_by_Date():
    print("\nSearch Expenses by Date")
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

#------------------------------------------------------------------------               
#                   MONTYLY SUMMARY            
def monthly_Summary():
    print("Monthly Summary")
    data = defaultdict(int)
    count=0
    total=0
    
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                amount, category, date = line.strip().split(",") 
                amount=int(amount)
                total+=amount
                count+=1
                data[category] += amount
            
        if(count==0):
            print("No data available")
            return
            
        average=total/count
        top_category = max(data, key=data.get)  
        
        print(f"Total Expenses : {total} PKR")  
        print(f"Entries : {count}")
        print(f"Average per Day :{average} PKR")
        print(f"TOP Category : {top_category}")       
        
    except FileNotFoundError:
        print("No data available.")    
        
#---------------------------------------------------------------
#                  MAIN MENU
def main_Menu():
    print(" EXPENSE TRACKER APP  ".center(50))
    print("-" * 50)
    
    while True:
       print("1) Add Expenses")
       print("2) View Expenses")
       print("3) Search Expenses by Date")
       print("4) Monthly Summary")
       print("5) EXIT")
    
       select=input("Select an option:")
       if(select=="1"):
           add_Expenses()    
                   
       elif(select=="2"):
           view_Expenses()    
                   
       elif(select=="3"):
           search_by_Date()    
                   
       elif(select=="4"):
           monthly_Summary()    
                   
       elif(select=="5"):
           print("THANKYOU so much! for Your Response.\n Have a Good Day")    
           break
       else:
           print("Invalid choice. Try again.")    
                 
if __name__ == "__main__":
    main_Menu()    
 #---------------------------END--------------------------------------                       
            
    

    

    


