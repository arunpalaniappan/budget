import db_access

def delete_account(user_name):
    user_name_from_user = input('To delete your account, enter user name: ')
    password_from_user = input('Enter account password: ')

    password = db_access.get_password(user_name)
    if user_name != user_name_from_user or \
       password != password_from_user:
        print ("Invalid Credentials")
        return
    else:
        return_value = db_access.delete_account(user_name)
        if return_value == 1:
            print ("Delete Successful")
            exit()
        else:
            print ("Deletion not successful. Try Again")
        return

    return
        
