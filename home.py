import sign_up_page
import login_page

def main():
    choice = int(input (
                        "\n1. Login"
			"\n2. Sign Up"
			"\n3. Exit"
			"\nGive your choice: "
			)
		)
    
    if choice == 1:  #login
        login_page.main()
    elif choice == 2:   #sign up
        sign_up_page.main()
    elif choice == 3:   #exit
        exit()
    else:
        print ('Invalid choice')
        exit()
