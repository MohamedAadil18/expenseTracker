options = {
    'A' : 'Add Expenses',
    'B' : 'Remove Expenses',
    'C' : 'Total Essential Expenses',
    'D' : 'Total Non-Essential Expenses',
    'E' : 'Total Monthly Expenses',
    'F' : 'Total Yearly expenses',
    'G' : 'Total Expenses',
    'H' : 'Display expenses'
}

class Expense:
    def __init__(self):
        self.expense_list = []
        
    def display_expense(self):
        if len(self.expense_list) > 0:
            for i in self.expense_list:
                for key,value in i.items():
                    print(f"{key} -> {value}")
                print("************************")
        else:
            print("\nExpense list is empty...")
        execute(user_name)

class manage_Expense:
    def add_expense(self,exp,user_name):
        add_again = 'y'
        while add_again == 'y':
            if len(user_name) <= 0:
                user_name = input("Enter your name: ")
        
            ess = input("Is it Essential? type (y/n)")
            if ess == 'y':
                category = 'essential'
            else:
                category = 'non-essential'
            name = input("Name of the thing you have spent on: ")
            price = int(input(f"Money spent on {name}: "))
            month = input("Month: ")
            year = int(input("Year: "))
            
            expense_dict = {
                'category' : category,
                'name' : name,
                'price' : price,
                'month' : month,
                'year' : year    
            }
            exp.expense_list.append(expense_dict)
            add_again = input("\nSuccessfully added expenses. Do you wish to Add something? type (y/n)").lower()
        
        execute(user_name)
        

    def remove_expense(self,exp,user_name):
        if len(user_name) < 1:
            user_name = input("Enter your name: ")
        if len(exp.expense_list) > 0:
            for i in range(0,len(exp.expense_list)):
                print(f"{i+1}. {exp.expense_list[i]}")
            
            remove_expense = int(input("Which one do you want to delete? enter the option: "))-1
            if remove_expense >= 0 and remove_expense < len(exp.expense_list):
                exp.expense_list.pop(remove_expense)
                
            print("\nExpense removed...!")
            
            if len(exp.expense_list) >= 0:
                print("Updated Expense list")
                for i in range(0,len(exp.expense_list)):
                    print(f"{i+1}. {exp.expense_list[i]}")
            else:
                print("\nNo expenses left in the list to display...")
        else:
            print("No expenses were present in the list")

        execute(user_name)        
        
class Expense_tracker:
    def essential_expense(self,exp,user_name):
        if len(user_name) < 1:
            user_name = input("Enter your name: ")
        if len(exp.expense_list) > 0:
            count = 0
            for i in exp.expense_list:
                if i['category'] == "essential":
                    count += i['price']
                    print(i)
            if count > 0:
                print(f"\nThe total amount spent on essentials is '{count}'")
            else:
                print("\nThere has been no spending on essential items...")
            
        else:
            print("No expenses were present in the list")
        
        execute(user_name)
                
    def non_essential_expense(self,exp,user_name):
        if len(user_name) < 1:
            user_name = input("Enter your name: ")
        if len(exp.expense_list) > 0:
            count = 0
            for i in exp.expense_list:
                if i['category'] == "non-essential":
                    count += i['price']
                    print(i)
            if count > 0:
                print(f"\n The total amount spent on non-essentials is '{count}'")
            else:
                print("\nThere has been no spending on non-essential items...")
                
        else:
            print("No expenses were present in the list")
        
        execute(user_name)
    
    def monthly_expense(self,exp,user_name,salary):
        if len(user_name) < 1:
            user_name = input("Enter your name: ")
            
        query = input("\nDo you want category wise monthly spendings? type (y/n)").lower()
        
        if len(exp.expense_list) > 0:
            if query == 'y':
                category = input("Enter the category (essential / non-essential): ")
                month = input("Enter a month: ")
            
                count = 0
                for i in exp.expense_list:
                    if i['category'] == category and i['month']  == month:
                        count += i['price']
                        print(i)
                        
                if count > 0:
                    print(f"\nThe total spending on {category}s in the month of {month} is {count}")
                    print(f"\nYou have spent {count} from your monthly salary {salary} on {category} things in the month {month}")
                else:
                    print(f"\nThere has been no records of spendings on {category}s in the month {month}")
                    
            elif query == 'n':
                month = input("Enter a month: ")
                count = 0
                for i in exp.expense_list:
                    if i['month'] == month:
                        count += i['price']
                        print(i)
                        
                if count > 0:
                    print(f"\nThe total spending in the month of {month} is {count}")
                    print(f"\nYou have spent {count} from your monthly salary {salary}. Remaining amount is {salary-count} from your monthly income")
                else:
                    print(f"\nThere has been no records of spendings in the month {month}")
            
            else:
                print("\nInvalid option...")
        else:
            print("No expenses were present in the list")
            
        execute(user_name)

    def yearly_expense(self,exp,user_name,salary):
        if len(user_name) < 1:
            user_name = input("Enter your name: ")
        
        query = input("\nDo you want category wise yearly spendings? type (y/n)").lower()
        if query == 'y':
            if len(exp.expense_list) > 0:
                category = input("Enter the category (essential / non-essential): ")
                year = int(input("Enter a year: "))
        
                count = 0
                for i in exp.expense_list:
                    if i['category'] == category and i['year'] == year:
                        count += i['price']
                        print(i)

                if count > 0:
                    print(f"\nThe total spending on {category}s in the year {year} is {count}")
                    print(f"\nYou have spent {count} from your yearly salary {salary} on {category} things in the year {year}")
                else:
                    print(f"\nThere has been no records of spendings on {category}s in the year {year}")
            else:
                print("No expenses were present in the list")
                
        elif query == 'n':
            if len(exp.expense_list) > 0:
                year = int(input("Enter a year: "))
                count = 0
                for i in exp.expense_list:
                    if i['year'] == year:
                        count += i['price']
                        print(i)
                        
                if count > 0:
                    print(f"\nThe total spending in the year {year} is {count}")
                    print(f"\nYou have spent {count} from your yearly salary {salary}. Remaining amount is {salary-count} from your yearly income")
                else:
                    print(f"\nThere has been no records of spendings in the year {year}")
            else:
                print("No expenses were present in the list")

        else:
            print("\nInvalid option...")
            
        execute(user_name)
        
    def total_expenses(self,exp,user_name):
        if len(user_name) < 1:
            user_name = input("Enter your name: ")
        if len(exp.expense_list) > 0:
            count = 0
            for i in exp.expense_list:
                count += i['price']
            
            if count > 0:
                print(f"\nThe total expenses spent from the starting till today is {count}")
            else:
                print(f"\nThere has been no records of spendings")
        else:
            print("No expenses were present in the list")

        execute(user_name)
        
user_name = input("enter your name: ")
salary_month = int(input("enter your monthly salary: "))
salary_year = int(input("enter your yearly salary: "))

def execute(user_name):
    print("\n")
    for i,j in options.items():
        print(f"{i}. {j}")

    opt = input("enter the option from the given above: ").upper()

    if opt == 'A':
        mng_exp.add_expense(exp,user_name)
    elif opt == 'B':
        mng_exp.remove_expense(exp,user_name)
    elif opt == 'C':
        exp_trac.essential_expense(exp,user_name)
    elif opt == 'D':
        exp_trac.non_essential_expense(exp,user_name)
    elif opt == 'E':
        exp_trac.monthly_expense(exp,user_name,salary_month)
    elif opt == 'F':
        exp_trac.yearly_expense(exp,user_name,salary_year)
    elif opt == 'G':
        exp_trac.total_expenses(exp,user_name)
    elif opt == 'H':
        exp.display_expense()
    else:
        print("Invalid option...")
        print("Program ends...")


exp = Expense()
mng_exp = manage_Expense()
exp_trac = Expense_tracker()
execute(user_name)