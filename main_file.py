# import packages
import mysql.connector
import register_process
import employee_action

# Database connecting 

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Astephen@28",
    database="employee_management"
)

mycursor=mydb.cursor()

def welcome_message():
    print(" Welcome to LS Tech employee's management  ".center(100))

def main_function():
    try:
        print("Enter Your Position  ")
        choice=int(input("   1 for HR \n   2 for Employee \n   3 for exit \nEnter here : "))
        if choice==1:
            try:
                def getting_need():
                    print("Enter the purpose of login")
                    user_in=int(input("   1 for Register \n   2 for Login \n   3 for exit \nEnter here : "))
                    if user_in==1:
                        try:
                            def getting_hr_details():
                                name=input("  Enter your name : ")
                                email=input("  Enter your email id : ")
                                branch=input("  Enter your branch : ")
                                register_process.registration(name,email,branch)
                        except Exception as e:
                            print("Enter required data ",e)
                            getting_hr_details()
                        getting_hr_details()
                    elif user_in==2:
                        register_process.login()
            except Exception as e:
                print("Invalid input ",e)
                getting_need()
            getting_need()
        elif choice==2:
            print(" You can see Your Details Here \n\n")
            employee_action.employee_act()
        else:
            print("Thanks for visiting!!")
    except Exception as e:
        print("Please Enter the correct choice",e)
        main_function()

if __name__=="__main__":
    welcome_message()
    main_function()