import db_access

def main(user_name):

    basic_choice = 1
    while (basic_choice > 0 and basic_choice < 6):
        basic_choice = int(input (
        "\n1. Income"
        "\n2. Expense"
        "\n3. Get balance"
        "\n4. Review and Prediction"
        "\n5. Exit"
        "\nGive your choice: "
        )
        )

        if basic_choice == 1:  #Income
            print ("Income")
            income_amount = float(input('Enter income amount: '))
            note = input('Note: ')
            db_access.income(user_name,income_amount,note)
            db_access.update_balance(user_name,income_amount,"income")


            

        elif basic_choice == 2:  #Expense
            print ("Expense")
            expense_category = int(input("\n1. Travel"
                                         "\n2. Food"
                                         "\n3. Bills"
                                         "\n4. Grossery"
                                         "\n5. Shopping"
                                         "\n6. Clothing"
                                         "\n7. Education"
                                         "\n8. Other Expense"
                                         "\nMake your choice: "
                                    )   )
            #Add a try except Value error block
            expense_amount = float(input("Enter expense: "))
            note = input("Note: ")
            if expense_category == 1:
                db_access.expense(user_name, expense_amount, "Travel" ,note)
                db_access.update_balance(user_name,expense_amount,"expense")
            elif expense_category == 2:
                db_access.expense(user_name, expense_amount, "Food" ,note)
                db_access.update_balance(user_name,expense_amount,"expense")
            elif expense_category == 3:
                db_access.expense(user_name, expense_amount, "Bills" ,note)
                db_access.update_balance(user_name,expense_amount,"expense")
            elif expense_category == 4:
                db_access.expense(user_name, expense_amount, "Grossery" ,note)
                db_access.update_balance(user_name,expense_amount,"expense")
            elif expense_category == 5:
                db_access.expense(user_name, expense_amount, "Shopping" ,note)
                db_access.update_balance(user_name,expense_amount,"expense")
            elif expense_category == 6:
                db_access.expense(user_name, expense_amount, "Clothing" ,note)
                db_access.update_balance(user_name,expense_amount,"expense")
            elif expense_category == 7:
                db_access.expense(user_name, expense_amount, "Education" ,note)
                db_access.update_balance(user_name,expense_amount,"expense")
            elif expense_category == 8:
                db_access.expense(user_name, expense_amount, "Other expense" ,note)
                db_access.update_balance(user_name,expense_amount,"expense")
            else:
                print ("Invalid choice ")	

        elif basic_choice == 3:   #Get balance
            print ("Balance")
            balance = db_access.get_balance(user_name)
            print ("Available balance is ",balance)

        elif basic_choice == 4:
            #Add prediction
            review.weekly_review(user_name)
            review.monthly_review(user_name)
            review.make_prediction(user_name)

        elif basic_choice == 5:
            exit()
        else:
            print ("Invalid choice")
