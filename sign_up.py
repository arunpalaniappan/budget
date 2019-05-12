##import mongo
##from expense_noter import Expense_Noter
##A new user will sign up.

import db_access
import expense_noter
import home
       
def password_check(password,confirm_password):
    if password == confirm_password:
        password_match = 1
        print ('Password matches')
    else:
        password_match = 0
        print ('Password is not matching')
        exit()
    return (password_match)

def main():
    print ("In sign up")
    user_name = input('Enter user name: ')
    #user_name = "arun"
    if (db_access.check_user_name(user_name)):
        password = input('Enter password: ')
        #password = "qwerty"
        confirm_password = input('Enter password again: ')
        #confirm_password = "qwerty"
        password_match = password_check(password,confirm_password)
        if password_check:
            db_access.sign_up(user_name,password)
            db_access.set_balance(user_name)  #Sets intial balance of Rs. 0 
            expense_noter.main(user_name)
        else:
            exit()
    else:
        print ('user name already exists ')
        home.main()
