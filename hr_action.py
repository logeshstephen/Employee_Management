import main_file
from tabulate import tabulate

def add_again():
    try:
        print("Do you want to add press 1 or exit 2 ")
        again=int(input("Enter here : "))
        if again==1:
            add_Emp_details()
        else:
            print("thanks for visiting!!")
    except Exception as e:
        print("Enter valid input",e)
        add_again()

def add_Emp_details():
    sql="Insert Into employee_details(emp_name,email,position,salary,branch) values(%s,%s,%s,%s,%s)"
    try: 
        emp_name=input("Enter Employee name : ")
        email=input("Enter the E-mail id : ")
        position=input("Enter employee position : ")
        salary=input("Enter the salary of : ")
        branch=input("Enter the branch name : ")
        if emp_name and email and position and salary and branch :
            values=(emp_name,email,position,salary,branch)
            main_file.mycursor.execute(sql,values)
            main_file.mydb.commit()
            print("Details successfully added")
            add_again()
        else:
            print("Enter the required details from else block")
            add_again()
    except Exception as e:
        print("Enter valid input ", e)
        add_again()


def read_emp_details():
    sql_all="Select * from employee_details"
    sql="Select * From employee_details Where emp_id=%s"
    try:
        print("  1 for view all employee details\n  2 for particular employee detail")
        hr_wants=int(input("Enter here : "))
        if hr_wants==1:
            main_file.mycursor.execute(sql_all)
            get_details=main_file.mycursor.fetchall()
            if get_details:
                col=[desc[0] for desc in main_file.mycursor.description]
                print(tabulate(get_details,headers=col,tablefmt="grid"))
        elif hr_wants==2:
            hr_read=int(input("Enter the employee id : "))
            main_file.mycursor.execute(sql,(hr_read,))
            get_details=main_file.mycursor.fetchall()
            if get_details:
                col=[desc[0] for desc in main_file.mycursor.description]
                print(tabulate(get_details,headers=col,tablefmt="grid"))
            else:
                print("no data")
            main_file.mydb.commit()
        else:
            print("Enter the correct value")
    except Exception as e:
        print("invalid input",e)

def update_emp_details():
    try:
        emp_name=input("Enter the employee name for update : ")
        print("Which column you want to change")
        print(" emp_id ")
        print(" emp_name ")
        print(" email ")
        print(" position ")
        print(" salary ")
        col_name=input("Enter here : ")
        hr_change=input(f"Enter the data for {col_name} : ")
        if emp_name and col_name and hr_change:
            sql=f"Update employee_details Set {col_name}=%s Where emp_name=%s"
            main_file.mycursor.execute(sql,(hr_change,emp_name,))
            main_file.mydb.commit()
            print("Update successful")
    except Exception as e:
        print("enter the column name correctly",e)

def remove_emp_details():
    sql="Delete From employee_details where emp_id=%s"
    try:
        hr_need=int(input("Enter the Employee id : "))
        if hr_need:
            main_file.mycursor.execute(sql,(hr_need,))
            main_file.mydb.commit()
            print("Employee details successfully Removed")
        else:
            print("No data found")
    except Exception as e:
        print("Invalid input",e)


def hr_activities():
    print("What you what to do : ")
    print(" 1 for Add employee details ")
    print(" 2 for Read details")
    print(" 3 for Update details")
    print(" 4 for Remove details")
    print(" 5 for Exit")
    hr_act=int(input("Enter here : "))
    if hr_act==1:
        add_Emp_details()
    elif hr_act==2:
        read_emp_details()
    elif hr_act==3:
        update_emp_details()
    elif hr_act==4:
        remove_emp_details()
    else:
        print("Thanks for Visiting")
    
    



if __name__=="__main__":
    main_file.welcome_message()
    main_file.main_function()