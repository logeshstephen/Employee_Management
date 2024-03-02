import main_file
from tabulate import tabulate

def employee_act():
    sql="Select * from employee_details Where emp_id=%s"
    try:
        emp_id=int(input("Enter Your id : "))
        main_file.mycursor.execute(sql,(emp_id,))
        get_details=main_file.mycursor.fetchall()
        if get_details:
            for i in get_details:
                print(f"\n\nHello {i[1].upper()} ,Your Details\n\n")
            col=[desc[0] for desc in main_file.mycursor.description]
            print(tabulate(get_details,headers=col,tablefmt="grid"))
        else:
            print("No data found")
    except Exception as e:
        print("Enter the valid details",e)

if __name__=="__main__":
    main_file.welcome_message()
    main_file.main_function()