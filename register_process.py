import main_file
import hr_action


def registration(name,email,branch):
    sql="Insert into hr_details(name,email,branch) values(%s,%s,%s)"
    value=(name,email,branch)
    main_file.mycursor.execute(sql,value)
    main_file.mydb.commit()
    print(f"Dear {name.upper()} your detail is successfully registered ")

    sql_read="Select * From hr_details Where name=%s"
    main_file.mycursor.execute(sql_read,(name,))
    hr_data=main_file.mycursor.fetchall()
    main_file.mydb.commit()
    for i in hr_data:
        print(f"keep your this '{i[0]}' id for login")
    def ask_for_login():
        try:
            hr_input=int(input("1 for Login \n2 for exit \nEnter here : "))
            if hr_input==1:
                login()
            else:
                print("Thanks for visiting!!!")
        except Exception as e:
            print("invalid input",e)
            ask_for_login()
    ask_for_login()
def login():
    sql="select hr_id,email from hr_details where hr_id=%s"
    try:
        hr_id=int(input("Enter your id number : "))
        name=input("Enter your name : ")
        email=input("Enter your email : ")
        if  hr_id !="" and email !="":
            main_file.mycursor.execute(sql,(hr_id,))
            data=main_file.mycursor.fetchall()
            if not data:
                print("No data found")
            else:
                for i in data:
                    if hr_id==i[0] and email==i[1]:
                        print(f"Hello {name.upper()} have successfully logged in !!!")
                        hr_action.hr_activities()
                        return
                print("sorry!! emial or name incorrect")
            main_file.mydb.commit()
        else:
            print("Enter the valid input")
    except Exception as e:
        print("Enter the valid details",e)

if __name__=="__main__":
    main_file.welcome_message()
    main_file.main_function()