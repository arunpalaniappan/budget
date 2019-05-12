import sign_up
import login

def main():
    choice = int(input (
                        "\n1. Login"
			"\n2. Sign Up"
                        "\n3. Delete Account"
			"\n4. Exit"
			"\nGive your choice: "
			)
		)
    
    if choice == 1:  #login
        login.main()
    elif choice == 2:   #sign up
        sign_up.main()
    elif choice == 3:
        #Yet to write code for deleting account
        print ("Yet to write function")
    elif choice == 4:   #exit
        exit()
    else:
        print ('Invalid choice')
        exit()
