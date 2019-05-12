#import mongo
import db_access
import expense_noter

def validate_password(password,db_password):
    if password == db_password:
        validate_password_result = 1
    else:
        validate_password_result = 0
    return (validate_password_result)
    
def main():
    user_name = input('Enter user name: ')
    #user_name = "arun"
    password = input('Enter password: ')
    #password = "qwerty"
    db_password = db_access.get_password(user_name)
    validate_password_result = validate_password(password,db_password)
    if validate_password_result:
        print ('Login successful')
        expense_noter.main(user_name)
    else:
        print ("Passwords don't match")
    exit()
